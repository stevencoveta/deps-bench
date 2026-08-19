from pydantic import BaseModel, root_validator, validator
from pydantic.error_wrappers import ValidationError


class RunBudget(BaseModel):
    balance_usd: float
    reserve_usd: float = 1.0
    concurrency: int = 1

    @validator("balance_usd")
    def balance_not_negative(cls, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        return value

    @root_validator
    def reserve_fits_balance(cls, values):
        if values.get("reserve_usd", 0.0) * values.get("concurrency", 1) > values.get("balance_usd", 0.0):
            raise ValueError("reserve exceeds balance")
        return values


def parse_budget(payload: dict) -> RunBudget:
    return RunBudget(**payload)


def budget_problem(payload: dict) -> str | None:
    try:
        RunBudget(**payload)
    except ValidationError as exc:
        return str(exc.errors()[0]["msg"])
    return None
