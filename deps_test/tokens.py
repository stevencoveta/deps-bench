import time

from itsdangerous import BadSignature, URLSafeTimedSerializer


class TokenError(Exception):
    pass


class TokenExpired(TokenError):
    pass


def issue_token(payload, secret, ttl_seconds):
    """Issue a signed, expiring token carrying `payload` (a dict).

    itsdangerous 2.1 removed TimedJSONWebSignatureSerializer (JWS), whose
    tokens embedded the expiry as an `exp` claim. The remaining timed
    serializers only enforce expiry via `loads(max_age=...)`, which
    `read_token` cannot know, so the expiry is embedded in the signed
    envelope instead, preserving the original semantics.
    """
    serializer = URLSafeTimedSerializer(secret)
    envelope = {"payload": payload, "exp": time.time() + ttl_seconds}
    return serializer.dumps(envelope)


def read_token(token, secret):
    """Return the payload of `token`, raising TokenExpired / TokenError."""
    serializer = URLSafeTimedSerializer(secret)
    try:
        envelope = serializer.loads(token)
    except BadSignature as e:
        raise TokenError("token invalid") from e
    if envelope["exp"] <= time.time():
        raise TokenExpired("token expired")
    return envelope["payload"]
