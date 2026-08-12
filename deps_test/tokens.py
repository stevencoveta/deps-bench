from itsdangerous import BadSignature, SignatureExpired, TimedJSONWebSignatureSerializer


class TokenError(Exception):
    pass


class TokenExpired(TokenError):
    pass


def issue_token(payload, secret, ttl_seconds):
    """Issue a signed, expiring token carrying `payload` (a dict)."""
    serializer = TimedJSONWebSignatureSerializer(secret, expires_in=ttl_seconds)
    return serializer.dumps(payload).decode("ascii")


def read_token(token, secret):
    """Return the payload of `token`, raising TokenExpired / TokenError."""
    serializer = TimedJSONWebSignatureSerializer(secret)
    try:
        return serializer.loads(token)
    except SignatureExpired as e:
        raise TokenExpired("token expired") from e
    except BadSignature as e:
        raise TokenError("token invalid") from e
