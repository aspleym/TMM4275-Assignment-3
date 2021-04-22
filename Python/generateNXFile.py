import os

# Name of project, not filename, e.g. maze


def createNXFile(name):
    script_dir = os.path.dirname(__file__)
    productsPath = "Products/"
    abs_file_path_template = os.path.join(
        script_dir[:len(script_dir) - 6], productsPath + "wcTemplate.py")

    prtPath = os.path.join(
        script_dir[:len(script_dir) - 6], productsPath + name + "/" + name + ".prt")

    f = open(abs_file_path_template, "r")
    txt = f.read()

    # .replace("\", "\\") IF NEEDED FOR PATHING IN WINDOWS
    txt = txt.replace("<<PATH>>", ("\""+prtPath+"\""), 1)
    f.close()

    f = open(prtPath[:len(prtPath) - 3] + "ini", "r")
    NAME = f.readline()
    NAME = NAME.split(": ")[1].rstrip()
    EMAIL = f.readline()
    EMAIL = EMAIL.split(": ")[1].rstrip()
    LENGTH = f.readline()
    LENGTH = LENGTH.split(": ")[1].rstrip()
    WIDTH = f.readline()
    WIDTH = WIDTH.split(": ")[1].rstrip()
    HEIGHT = f.readline()
    HEIGHT = HEIGHT.split(": ")[1].rstrip()
    f.close()

    txt = txt.replace("<<BOTSIZE>>", f'{LENGTH}, {WIDTH}, {HEIGHT}')

    f = open(prtPath[:len(prtPath) - 3] + "py", "w")
    f.write(txt)
    f.close()
