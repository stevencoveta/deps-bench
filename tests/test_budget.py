import pytest

from deps_test.budget import budget_problem, parse_budget


def test_a_funded_budget_parses_and_coerces():
    assert parse_budget({"balance_usd": 3}).reserve_usd == 1.0
    assert parse_budget({"balance_usd": "2.5"}).balance_usd == 2.5


def test_negative_balance_is_rejected():
    assert "balance cannot be negative" in (budget_problem({"balance_usd": -1}) or "")


def test_reserve_must_fit_the_balance_across_concurrency():
    assert budget_problem({"balance_usd": 3, "reserve_usd": 2, "concurrency": 2}) == "reserve exceeds balance"
    assert budget_problem({"balance_usd": 4, "reserve_usd": 2, "concurrency": 2}) is None


def test_validation_errors_raise_the_pydantic_type():
    with pytest.raises(Exception) as exc_info:
        parse_budget({"balance_usd": -5})
    assert exc_info.type.__name__ == "ValidationError"
