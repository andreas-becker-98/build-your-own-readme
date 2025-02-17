from os.path import dirname, isfile, join, exists
from os import getcwd, mkdir


def read_file(file_name: str) -> str | None:
    abs_file_path = join(dirname(__file__), file_name)

    if not isfile(abs_file_path):
        return None
    
    with open(abs_file_path) as file:
        return file.read()


def is_running_in_project_folder():
    return getcwd() == dirname(__file__);

def create_output_folder():
    if not exists("./output"):
        mkdir("./output")