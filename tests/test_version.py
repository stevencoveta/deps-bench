from deps_test.version import is_supported, requests_version


def test_version_is_dotted_string():
    version = requests_version()
    assert isinstance(version, str)
    assert version.count(".") >= 1


def test_support_floor_and_ceiling():
    assert is_supported(2) is True
    assert is_supported(99) is False
