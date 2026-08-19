from werkzeug.urls import url_quote, url_unquote


def share_link(base: str, title: str) -> str:
    return f"{base.rstrip('/')}/s/{url_quote(title, safe='')}"


def link_title(link: str) -> str:
    return url_unquote(link.rsplit("/", 1)[-1])
