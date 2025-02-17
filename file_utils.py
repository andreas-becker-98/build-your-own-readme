from os.path import dirname, isfile, join


def read_file(file_name: str) -> str | None:
    abs_file_path = join(dirname(__file__), file_name)

    if not isfile(abs_file_path):
        return None
    
    with open(abs_file_path) as file:
        return file.read()