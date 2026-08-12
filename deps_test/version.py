import requests


def requests_version() -> str:
    return requests.__version__


def is_supported(min_major: int = 2) -> bool:
    return int(requests.__version__.split(".")[0]) >= min_major
