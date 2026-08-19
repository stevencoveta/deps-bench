from pydantic import BaseModel, ValidationError, field_validator, model_validator


class RunBudget(BaseModel):
    balance_usd: float
    reserve_usd: float = 1.0
    concurrency: int = 1

    @field_validator("balance_usd")
    @classmethod
    def balance_not_negative(cls, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        return value

    @model_validator(mode="after")
    def reserve_fits_balance(self):
        if self.reserve_usd * self.concurrency > self.balance_usd:
            raise ValueError("reserve exceeds balance")
        return self


def parse_budget(payload: dict) -> RunBudget:
    return RunBudget(**payload)


def budget_problem(payload: dict) -> str | None:
    try:
        RunBudget(**payload)
    except ValidationError as exc:
        error = exc.errors()[0]
        # In pydantic v2, messages of errors raised from validators are
        # prefixed with "Value error, "; the original exception message is
        # kept in the error context. Unwrap it to keep the v1 behaviour.
        cause = error.get("ctx", {}).get("error")
        if isinstance(cause, ValueError):
            return str(cause)
        return str(error["msg"])
    return None
