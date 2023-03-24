import glob
import os
import os.path
import shutil
from pathlib import Path
import re

#1
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
        time = old_name.split("_")[2]
        type_of_tree = old_name.split("_")[3].split("-")[0]
        col = old_name.split("_")[3].split("-")[1]
        line = old_name.split("_")[3].split("-")[2]
        if line.find("b") != -1:
            rl = "R"
            line = line.replace("b", "")
        else:
            rl = "L"
        position_of = (col + "-" + line + "-" + rl).replace(".jpeg", "")

        dest = os.path.join(dire, "{}_{}_{}_{}_{}.{}".format(orchard, date, time, position_of, type_of_tree,extension))
        print(dest)
        # copying file to TARGET destination with new name
        #shutil.copy2(file, dest)
#2
def copy_and_rename_files2(dire, extension):
    """
        Renaming to "orchard_date_time_position".
        Copy file to new location with new name.
        From old_naming convention --> b is new R, nothing is new L
    """
    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)

    for file in files:  # Naming of file
        old_name = Path(file).name
        old_name_list = re.split("_", old_name)
        old_name_list[-1] = old_name_list[-1].replace(".jpeg", "")

        sad = "troja"
        date = old_name_list[0].replace("p", "")
        time = old_name_list[1]

        # different naming at the end --> usually with or without type of three
        if len(old_name_list[2].split("-")) > 2:
            type_of_tree = old_name_list[2].split("-")[0]
            row = old_name_list[2].split("-")[1]
            number_of_tree = old_name_list[2].split("-")[2]
        else:
            type_of_tree = ""
            row = old_name_list[2].split("-")[0]
            number_of_tree = old_name_list[2].split("-")[1]

        # left or right position
        if ((row + number_of_tree).find("b")) != -1:
            rl = "R"
            number_of_tree = number_of_tree.replace("b", "")
            row = row.replace("b", "")
        else:
            rl = "L"

        position_of = row + "-" + number_of_tree + "-" + rl

        # copying file to TARGET
        dest = os.path.join(dire, "{}_{}_{}_{}_{}.{}".format(sad, date, time, position_of, type_of_tree, extension))
        print(dest)
        #shutil.copy2(file, dest)

    # 3a
    def rename_existing_files3(dire, extension):
        glob_path = "{}/**/*.{}".format(dire, extension)
        files = glob.glob(glob_path, recursive=True)
        for file in files:
            """
            Load place, date, time, pos. of tree to variable - place and date from parent.parent files name (or written), 
                time and location of tree from parent files name.
            Save file to new location with new name.
            """

            # Naming of file
            f1 = Path(file)
            sad_date_time_type_position = f1.name
            # x = re.search("[a-z]+_[0-9]+_[a-zA-Z]+-[a-zA-Z0-9]+", sad_date_time_type_position)
            # if x is not None:
            str_array = re.split("_", sad_date_time_type_position)
            str_array[-1] = str_array[-1].replace(".jpg", "")

            sad = str_array[1]
            date_of = str_array[2]
            time_of = str_array[3]
            type_of = str_array[4]
            position_of_old = str_array[5]

            x = re.search("[A-Z]", str_array[5])
            row = str_array[5][:x.start()]
            numberoftree = str_array[5][x.end():]
            rl = str_array[5][x.start():x.end()]
            position_of = row + "-" + numberoftree + "-" + rl

            dest = os.path.join(TARGET,
                                "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of, extension))
            print(dest)
            # shutil.copy2(file, dest)

    # 3b ten je asi spatne
    def rename_existing_files4(dire, extension):
        glob_path = "{}/**/*.{}".format(dire, extension)
        files = glob.glob(glob_path, recursive=True)
        for file in files:
            """
            Load place, date, time, pos. of tree to variable - place and date from parent.parent files name (or written), 
                time and location of tree from parent files name.
            Save file to new location with new name.
            """
            # Naming of file
            f1 = Path(file)
            sad_date_time_type_position = f1.name
            sad_date_time_type_position = sad_date_time_type_position.split("_")[0]

            str_array = re.split("_", sad_date_time_type_position)
            str_array[-1] = str_array[-1].replace(".jpg", "")

            sad = str_array[1]
            date_of = str_array[2]
            time_of = str_array[3]
            type_of = str_array[4]
            position_of_old = str_array[5]

            x = re.search("[A-Z]", str_array[5])
            row = str_array[5][:x.start()]
            numberoftree = str_array[5][x.end():]
            rl = str_array[5][x.start():x.end()]
            position_of = row + "-" + numberoftree + "-" + rl

            # copying file to TARGET
            dest = os.path.join(TARGET,
                                "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of, extension))
            print(dest)
            # shutil.copy2(file, dest)
