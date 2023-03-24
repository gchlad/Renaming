import glob
import os
import os.path
import shutil
from pathlib import Path
import re

TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection"
# SOURCE = "C:/Users/Gabriela/Documents/220920-holo"
SOURCE = r"C:/Users/Gabriela/Downloads/datasety/dataset_v1" # 508
#z troji, b je R, nic je L
# SOURCE = "220920-holo"
# TARGET = "collection"

def rename_existing_files2 (dire, extension):
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
        sad_date_time_type_position = f1.name
        # x = re.search("[a-z]+_[0-9]+_[a-zA-Z]+-[a-zA-Z0-9]+", sad_date_time_type_position)
        # if x is not None:
        str_array = re.split("_", sad_date_time_type_position)
        str_array[-1]=str_array[-1].replace(".jpeg","")
        print(str_array)

        sad = "troja"
        date_of = str_array[0]
        date_of=date_of.replace("p", "")
        time_of = str_array[1]



        if len(str_array[2].split("-")) > 2:
            type_of = str_array[2].split("-")[0]
            row = str_array[2].split("-")[1]
            numberoftree = str_array[2].split("-")[2]
        else:
            type_of = ""
            row = str_array[2].split("-")[0]
            numberoftree = str_array[2].split("-")[1]

        print(numberoftree)
        print(row)
        print((row+numberoftree).find("b"))
        if ((row+numberoftree).find("b")) != -1:
            rl = "R"
            numberoftree = numberoftree.replace("b", "")
            row = row.replace("b", "")
            #position_of = row + "-" + numberoftree + "-" + rl
        else:
            rl = "L"
            #position_of = row + "-" + numberoftree + "-" + rl

        position_of = row + "-" + numberoftree + "-" + rl

        #print(numberoftree)
        """
        if numberoftree.find("b") != -1:
            rl = "R"
            numberoftree = numberoftree.replace("b", "")
        else:
            rl = "L"
        position_of = row+"-"+numberoftree+"-"+rl
        """
        # copying file to TARGET
        #print(sad_date_time_type_position)
        #print(sad)
        #print(date_of)
        #print(time_of)
        #print(type_of)
        #print(position_of)

        dest = os.path.join(TARGET, "{}_{}_{}_{}_{}.{}".format(sad, date_of, time_of, position_of, type_of,extension))
        print(dest)
        shutil.copy2(file, dest)

if __name__ == "__main__":
    rename_existing_files2(SOURCE, "jpeg")




