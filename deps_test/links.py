from urllib.parse import quote as _url_quote, unquote as _url_unquote

# werkzeug 2.2.x's ``url_quote`` never percent-encoded these RFC 3986
# sub-delimiters (its ``_always_safe`` set), even when called with
# ``safe=''``. ``werkzeug.urls.url_quote``/``url_unquote`` were deprecated in
# werkzeug 2.3 and removed in 3.0 in favor of ``urllib.parse``, whose ``quote``
# only keeps ``A-Za-z0-9_.-~`` plus its ``safe`` argument. Passing these extra
# characters as ``safe`` preserves the exact encoding behavior of the old call.
_WERKZEUG_ALWAYS_SAFE = "$!'()*+,;"


def share_link(base: str, title: str) -> str:
    return f"{base.rstrip('/')}/s/{_url_quote(title, safe=_WERKZEUG_ALWAYS_SAFE)}"


def link_title(link: str) -> str:
    return _url_unquote(link.rsplit("/", 1)[-1])
