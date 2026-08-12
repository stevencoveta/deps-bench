import time

import pytest

from deps_test.tokens import TokenError, TokenExpired, issue_token, read_token

SECRET = "fixture-secret"


def test_round_trip():
    token = issue_token({"user": "ada", "role": "admin"}, SECRET, ttl_seconds=60)
    assert read_token(token, SECRET) == {"user": "ada", "role": "admin"}


def test_expired_token_raises():
    token = issue_token({"user": "ada"}, SECRET, ttl_seconds=1)
    time.sleep(2)
    with pytest.raises(TokenExpired):
        read_token(token, SECRET)


def test_tampered_token_rejected():
    token = issue_token({"user": "ada"}, SECRET, ttl_seconds=60)
    with pytest.raises(TokenError):
        read_token(token[:-2] + "xx", SECRET)


def test_wrong_secret_rejected():
    token = issue_token({"user": "ada"}, SECRET, ttl_seconds=60)
    with pytest.raises(TokenError):
        read_token(token, "other-secret")
