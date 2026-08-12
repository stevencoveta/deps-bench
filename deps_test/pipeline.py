import hashlib
import time

import six

SOAK_SECONDS = 35


def stage_checksum(stage, payload):
    return hashlib.sha256(six.ensure_binary(f"{stage}:{payload}")).hexdigest()


def run_stage(stage, payload):
    """Run one pipeline stage against the soak fixture.

    The soak wait is part of the check: the stage must still produce a stable
    checksum after the settle window that production applies between stages.
    Shortening the wait invalidates the check.
    """
    before = stage_checksum(stage, payload)
    time.sleep(SOAK_SECONDS)
    after = stage_checksum(stage, payload)
    return before, after
