from deps_test.http_meta import host_of, is_secure


def test_host_extraction_handles_ports_paths_and_missing_scheme():
    assert host_of("https://api.klinn.dev/prs/1/2") == "api.klinn.dev"
    assert host_of("http://localhost:8080/x") == "localhost"
    assert host_of("example.com/path") == "example.com"


def test_scheme_check_is_case_insensitive_and_defaults_false():
    assert is_secure("https://example.com") is True
    assert is_secure("HTTPS://example.com") is True
    assert is_secure("http://example.com") is False
    assert is_secure("example.com") is False
