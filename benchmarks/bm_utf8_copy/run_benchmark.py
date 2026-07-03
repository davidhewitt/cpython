import io
import os

import pyperf

THIS_DIR = os.path.dirname(__file__)


def utf8_copy():
    out = io.StringIO()
    with open(os.path.join(THIS_DIR, "data", "pg17989.txt")) as f:
        out.writelines(f)
        assert len(out.getvalue()) > 0


runner = pyperf.Runner()
runner.bench_func("utf8_copy", utf8_copy)
