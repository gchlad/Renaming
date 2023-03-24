import glob
import os
import os.path
import shutil
from pathlib import Path
import re

TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection"
# SOURCE = "C:/Users/Gabriela/Documents/220920-holo"
SOURCE = r"C:/Users/Gabriela/Downloads/datasety"
# SOURCE = "220920-holo"
# TARGET = "collection"

def copy_and_rename_dataset (dire, extension):
    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)
    for file in files:
        print(file)
        """
        Load place, date, time, pos. of tree to variable - place and date from parent.parent files name (or written), 
            time and location of tree from parent files name.
        Save file to new location with new name.
        """

        # Naming of file
        f1 = Path(file)
        time_type_position = f1.parent.name
        x = re.search("[0-9]+_[a-zA-Z]+-[a-zA-Z0-9]+", time_type_position)
        if x is not None:
            time_of_img = time_type_position.split("_")[0]
            type_of_tree = time_type_position.split("_")[1].split("-")[0]
            # position_of_tree = time_type_position.split("-")[0]
            position_of_tree = time_type_position.split("_")[1].split("-")[1]

            sad = "holovousy"
            date = 220920 # or take name1=f1.parent.parent.name and get date from that

            # copying file to TARGET
            print(time_type_position)
            print(sad)
            print(date)
            print(time_of_img)
            print(type_of_tree)
            print(position_of_tree)
            dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date, time_of_img, type_of_tree, position_of_tree,
                                                                   extension))
            # print(dest)
            shutil.copy2(file, dest)

if __name__ == "__main__":
    copy_and_rename_dataset(SOURCE, "jpeg")



