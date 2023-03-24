import glob
import os
import os.path
import shutil
from pathlib import Path
import re


def copy_and_rename_files (dire, extension):
    """
          Renaming to "orchard_date_time_position".
          Copy file to new location with new name.
          From old_naming convention --> b is new R, nothing is new L
    """
    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)

    for file in files:         # Naming of file
        old_name = Path(file).name

        orchard = old_name.split("_")[0]
        date = (old_name.split("_")[1])[1:]
        time_of = old_name.split("_")[2]
        type_of = old_name.split("_")[3].split("-")[0]
        col = old_name.split("_")[3].split("-")[1]
        line = old_name.split("_")[3].split("-")[2]
        if line.find("b") != -1:
            rl = "R"
            line = line.replace("b", "")
        else:
            rl = "L"
        position_of = (col + "-" + line + "-" + rl).replace(".jpeg", "")

        dest = os.path.join(dire, "{}_{}_{}_{}_{}.{}".format(orchard, date, time_of, position_of, type_of,extension))
        print(dest)

        # copying file to TARGET destination with new name
        #shutil.copy2(file, dest)
