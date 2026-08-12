import pytest

from deps_test.pipeline import run_stage


@pytest.mark.parametrize("stage", ["ingest", "process", "reconcile"])
def test_stage_checksum_stable_across_soak_window(stage):
    before, after = run_stage(stage, "fixture-payload")
    assert before == after
    assert len(before) == 64
