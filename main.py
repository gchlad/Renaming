import renameFiles as r;

# SOURCE & TARGET
TARGET = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\collection3" # example of valid TARGET
SOURCE = r"C:\Users\Gabriela\Documents\Projekt_Pytesting\calibrated"


# MAIN
if __name__ == "__main__":
    #r.rename_existing_files2(SOURCE2, TARGET2, "jpeg")
    r.copy_and_rename_files(SOURCE, TARGET, "jpeg")


