from deps_test.links import link_title, share_link


def test_share_link_percent_encodes_reserved_characters():
    assert share_link("https://reports.example", "weekly build & deploy") == (
        "https://reports.example/s/weekly%20build%20%26%20deploy"
    )
    assert share_link("https://reports.example/", "a/b c") == "https://reports.example/s/a%2Fb%20c"


def test_share_link_encodes_unicode_as_utf8():
    assert share_link("https://x.io", "café") == "https://x.io/s/caf%C3%A9"


def test_share_link_survives_a_round_trip():
    for title in ("plain", "space here", "café & crème", "slash/inside"):
        assert link_title(share_link("https://x.io", title)) == title
