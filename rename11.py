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

#2
def rename_existing_files2 (dire, extension):
    # b is R, nothing is L
    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)
    for file in files:
        # Naming of file
        f1 = Path(file)
        old_name = f1.name
        whole_name = re.split("_", old_name)
        whole_name[-1]=whole_name[-1].replace(".jpeg", "")

        sad = "troja"
        date_of = whole_name[0]
        date_of = date_of.replace("p", "")
        time_of = whole_name[1]

        if len(whole_name[2].split("-")) > 2:
            type_of = whole_name[2].split("-")[0]
            row = whole_name[2].split("-")[1]
            numberoftree = whole_name[2].split("-")[2]
        else:
            type_of = ""
            row = whole_name[2].split("-")[0]
            numberoftree = whole_name[2].split("-")[1]

        if ((row+numberoftree).find("b")) != -1:
            rl = "R"
            numberoftree = numberoftree.replace("b", "")
            row = row.replace("b", "")
        else:
            rl = "L"
        position_of = row + "-" + numberoftree + "-" + rl

        # copying file to TARGET
        dest = os.path.join(TARGET2, "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of,extension))
        print(dest)
        shutil.copy2(file, dest)

#3a
def rename_existing_files3 (dire, extension):
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
        str_array[-1]=str_array[-1].replace(".jpg", "")

        sad = str_array[1]
        date_of = str_array[2]
        time_of = str_array[3]
        type_of = str_array[4]
        position_of_old = str_array[5]

        x = re.search("[A-Z]", str_array[5])
        row = str_array[5][:x.start()]
        numberoftree = str_array[5][x.end():]
        rl=str_array[5][x.start():x.end()]
        position_of = row + "-" + numberoftree + "-" + rl

        dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of, extension))
        print(dest)
        #shutil.copy2(file, dest)


#3b ten je asi spatne
def rename_existing_files4 (dire, extension):
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
        str_array[-1]=str_array[-1].replace(".jpg", "")

        sad = str_array[1]
        date_of = str_array[2]
        time_of = str_array[3]
        type_of = str_array[4]
        position_of_old = str_array[5]

        x = re.search("[A-Z]", str_array[5])
        row = str_array[5][:x.start()]
        numberoftree = str_array[5][x.end():]
        rl=str_array[5][x.start():x.end()]
        position_of = row + "-" + numberoftree + "-" + rl

        # copying file to TARGET
        dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of, extension))
        print(dest)
        #shutil.copy2(file, dest)

#MAIN
"""
if __name__ == "__main__":
    #rename_existing_files(SOURCE, "jpeg")
    #rename_existing_files2(SOURCE2, "jpeg")
    rename_existing_files3(SOURCE3, "jpg")
"""