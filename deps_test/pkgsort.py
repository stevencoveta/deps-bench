from packaging.version import InvalidVersion, parse


def sort_releases(tags):
    """Sort release tags newest-first.

    Tags that are not valid PEP 440 versions (old CI tags like "banana-rc" or
    "2.x") must not be dropped: they sort after all real versions, alphabetically.
    """
    real = []
    legacy = []
    for tag in tags:
        try:
            real.append((parse(tag), tag))
        except InvalidVersion:
            legacy.append(tag)
    return [tag for _, tag in sorted(real, key=lambda pair: pair[0], reverse=True)] + sorted(legacy)
