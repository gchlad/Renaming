import glob
import os
import os.path
import shutil
from pathlib import Path

TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection2"
SOURCE = r"C:/Users/Gabriela/Downloads/datasety/dataset_v2"

def rename_existing_files (dire, extension):
    """
          Load location, date, time, position of tree, time and location of tree from parent files name.
          Save file to new location with new name.
    """

    glob_path = "{}/**/*.{}".format(dire, extension)
    files = glob.glob(glob_path, recursive=True)
    for file in files:
        # Getting new name
        f1 = Path(file)
        sad_date_time_type_position = f1.name
        # x = re.search("[a-z]+_[0-9]+_[a-zA-Z]+-[a-zA-Z0-9]+", sad_date_time_type_position)
        # if x is not None:
        sad = sad_date_time_type_position.split("_")[0]
        date_of = sad_date_time_type_position.split("_")[1]
        date_of_new = date_of[1:]
        time_of = sad_date_time_type_position.split("_")[2]

        type_of = sad_date_time_type_position.split("_")[3].split("-")[0]
        col = sad_date_time_type_position.split("_")[3].split("-")[1]
        line = sad_date_time_type_position.split("_")[3].split("-")[2]
        if line.find("b") != -1:
            rl = "R"
            line = line.replace("b", "")
        else:
            rl = "L"
        position_of = (col + "-" + line + "-" + rl).replace(".jpeg", "")

        # copying file to TARGET
        print(sad_date_time_type_position)
        #print(sad)
        #print(date_of_new)
        #print(time_of)

        #print(type_of)
        print(position_of)
        dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date_of_new, time_of, position_of, type_of,extension))
        print(dest)
        shutil.copy2(file, dest)

if __name__ == "__main__":
    rename_existing_files(SOURCE, "jpeg")




