from packaging.version import LegacyVersion, parse


def sort_releases(tags):
    """Sort release tags newest-first.

    Tags that are not valid PEP 440 versions (old CI tags like "banana-rc" or
    "2.x") must not be dropped: they sort after all real versions, alphabetically.
    """
    parsed = [(parse(tag), tag) for tag in tags]
    real = [(version, tag) for version, tag in parsed if not isinstance(version, LegacyVersion)]
    legacy = [tag for version, tag in parsed if isinstance(version, LegacyVersion)]
    return [tag for _, tag in sorted(real, key=lambda pair: pair[0], reverse=True)] + sorted(legacy)
