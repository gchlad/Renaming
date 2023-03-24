import glob
import os
import os.path
import shutil
from pathlib import Path
import re

TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection2"
SOURCE = r"C:/Users/Gabriela/Downloads/datasety/dataset_v2" # existing dataset

TARGET2 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection"
SOURCE2 = r"C:/Users/Gabriela/Downloads/datasety/dataset_v1" # existing dataset

TARGET3 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection3"
SOURCE3 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\calibrated" # added

#1
def rename_existing_files (dire, extension):
    """
          Get location, date, time, position of tree in image.
          Copy file to new location with new name.
          From old_name b is R, nothing is L
    """
    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)
    for file in files:
        # Naming of file
        f1 = Path(file)
        old_name = f1.name

        sad = old_name.split("_")[0]
        date_of = old_name.split("_")[1]
        date_of_new = date_of[1:]
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

        dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date_of_new, time_of, position_of, type_of,extension))
        # print(dest)
        # copying file to TARGET destination with new name
        shutil.copy2(file, dest)
