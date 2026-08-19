from urllib3.util import parse_url


def host_of(url: str) -> str:
    return parse_url(url).host or ""


def is_secure(url: str) -> bool:
    return (parse_url(url).scheme or "").lower() == "https"
