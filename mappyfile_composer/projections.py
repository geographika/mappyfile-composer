"""
Gather all projections from a Mapfile and write them to a minimal projection file
"""
import os
from itertools import groupby

def create_projection_files(projections, input_folder, output_fld):
    """
    Loading the full EPSG file can slow performance down
    Extract all EPSG codes from within the Mapfile and create a minimal EPSG file
    """

    files = []

    for key, group in groupby(projections, lambda prj: prj.split(":")[0]):
        fn = os.path.join(output_fld, key)
        files.append(fn)
        with open(fn, "w") as f:
            for p in group:
                prj = get_projection_from_file(input_folder, p)
                f.write(prj + "\n")

    return files

def get_projection_from_file(fld, proj):

    fn, code = proj.split(":")
    proj_file = os.path.join(fld, fn)
    with open(proj_file) as f:
        lines = f.read().splitlines()
        tag = "<{}>".format(code)
        pl = [l for l in lines if l.startswith(tag)]
        if pl:
            prj_spec = pl[0].strip()
        else:
            raise KeyError("The projection {} was not found in {}".format(proj, proj_file))

    return prj_spec


def get_mapfile_projections(m):
    """
    Return a list of unique projection codes in the Mapfile
    """

    projections = get_composite_projections(m)

    if "layers" in m:
        for l in m["layers"]:
            projections += get_composite_projections(l)

    return sorted(set(projections))

def get_composite_projections(d):

    projections = []
    p = get_projection(d)
    if p:
        projections.append(p)

    if "metadata" in d:
        projections += get_metadata_projections(d["metadata"])

    return sorted(set(projections))

def get_projection(d):
    """
    + MAP PROJECTION
    + LAYER PROJECTION
    + METADATA
    """
    if "projection" in d:
        prj = d["projection"]
        if len(prj) == 1:
             p = prj[0].lower()
             if "init" in p:
                return p.split("init=")[1]

def get_metadata_projections(md):

    keys = ["wms_srs", "ows_srs", "wfs_srs"]
    projections = []

    for k in keys:
        if k in md:
            projections += md[k].lower().split()

    return sorted(set(projections))
