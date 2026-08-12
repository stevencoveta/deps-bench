from deps_test.pkgsort import sort_releases


def test_newest_first():
    assert sort_releases(["1.0.0", "2.1.0", "2.0.3"]) == ["2.1.0", "2.0.3", "1.0.0"]


def test_legacy_tags_sort_last_not_dropped():
    assert sort_releases(["banana", "1.2.0", "2.x", "0.9"]) == ["1.2.0", "0.9", "2.x", "banana"]


def test_prereleases_order_within_reals():
    assert sort_releases(["1.0.0rc1", "1.0.0", "legacy-tag"]) == ["1.0.0", "1.0.0rc1", "legacy-tag"]
