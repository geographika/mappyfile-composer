import os
import mappyfile
from mappyfile_composer import symbols
import pytest


def test_get_symbols():

    s = """
    MAP
        PROJECTION
            "init=epsg:23700"
        END
    END
    """
    m = mappyfile.loads(s)
    prj = projections.get_projection(m)
    print(prj)
    assert(prj == "epsg:23700")


def run_tests():
    pytest.main(["tests/test_symbols.py", "-vv"])


if __name__ == '__main__':
    test_create_projection_files()
    run_tests()
    print("Done!")
