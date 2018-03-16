import os
import mappyfile
from mappyfile_composer import projections
import pytest


def test_get_projection():

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


def test_get_metadata_projection():

    s = """
    METADATA
      "wms_title"     "WMS Demo Server"
      "wms_srs"       "EPSG:42304 EPSG:42101 EPSG:4269 EPSG:4326"
      "ows_srs"       "epsg:3857 EPSG:42101"
      "wms_enable_request" "*"
    END
    """
    m = mappyfile.loads(s)
    prjs = projections.get_metadata_projections(m)
    print(prjs)
    assert(prjs == ['epsg:3857', 'epsg:42101', 'epsg:42304', 'epsg:4269', 'epsg:4326'])


def test_get_mapfile_projections():

    s = """
    MAP
        PROJECTION
            "init=epsg:23700"
        END
        METADATA
          "wms_srs"       "EPSG:4230 EPSG:4210 EPSG:4269 EPSG:4326"
          "ows_srs"       "epsg:3857 EPSG:42101"
        END
        LAYER
            PROJECTION
                "init=epsg:23700"
            END
            METADATA
                "wfs_srs"       "EPSG:4136 EPSG:29902"
                "ows_srs"       "epsg:3857 EPSG:4210"
            END
        END
    END
    """
    m = mappyfile.loads(s)
    prjs = projections.get_mapfile_projections(m)
    print(prjs)
    assert(prjs == ['epsg:23700', 'epsg:29902', 'epsg:3857', 'epsg:4136', 'epsg:4210', 'epsg:42101', 'epsg:4230', 'epsg:4269', 'epsg:4326'])


def test_get_projection_from_file():
    
    fld = os.path.join(os.path.dirname(__file__), "projections")
    prj = projections.get_projection_from_file(fld, 'epsg:29902')

    assert(prj == "<29902> +proj=tmerc +lat_0=53.5 +lon_0=-8 +k=1.000035 +x_0=200000 +y_0=250000 +datum=ire65 +units=m +no_defs  <>")



def test_create_projection_files():

    input_fld = os.path.join(os.path.dirname(__file__), "projections")
    output_fld = os.path.dirname(__file__)
    prjs = ['epsg:23700', 'epsg:29902', 'epsg:3857', 'epsg:4136', 'epsg:4210', 'epsg:4230', 'epsg:4269', 'epsg:4326']
    files = projections.create_projection_files(prjs, input_fld, output_fld)
    print(files)


def run_tests():
    pytest.main(["tests/test_projections.py", "-vv"])


if __name__ == '__main__':
    test_create_projection_files()
    run_tests()
    print("Done!")
