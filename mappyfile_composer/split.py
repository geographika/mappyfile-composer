import os
import mappyfile
from mappyfile.pprint import Quoter

        
def read_mapfile(fn, output_folder):

    
    mf = mappyfile.load(fn)
    quoter = Quoter()
    includes = []

    for l in (mf["layers"]):
        layer_file = quoter.remove_quotes(l["name"]) + ".txt"
        ofn = os.path.join(output_folder, layer_file)
        mappyfile.write(l, ofn)
        includes.append(quoter.add_quotes(layer_file))

    # now write the mapfile with includes
    ofn = os.path.join(output_folder, "_" + os.path.basename(fn))
    del mf["layers"]

    existing_includes = mf["include"]

    if (len(existing_includes)) > 0:
        mf["include"] += includes
    else:
        mf["include"] = includes

    mappyfile.write(mf, ofn)

if __name__ == "__main__":
    fn = r"C:\MapServer\apps\prime2\maps\prime2.map"
    output_folder = r"C:\MapServer\apps\prime2\maps\split"
    read_mapfile(fn, output_folder)
    print("Done!")