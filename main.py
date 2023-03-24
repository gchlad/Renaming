import rename11 as r;

# MAIN

TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection2"
SOURCE = r"C:/Users/Gabriela/Downloads/datasety/dataset_v2" # existing dataset

TARGET2 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection"
SOURCE2 = r"C:/Users/Gabriela/Downloads/datasety/dataset_v1" # existing dataset

TARGET3 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection3"
SOURCE3 = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\calibrated" # added

if __name__ == "__main__":
    #copy_and_rename_dataset(SOURCE, "jpeg")

    #rename_existing_files(SOURCE, "jpeg")
    #rename_existing_files2(SOURCE2, "jpeg")
    r.rename_existing_files3(SOURCE3, "jpg")


