from pathlib import Path


def open_file_line_list(filename: Path) -> list:
    with open(filename, 'r') as fileobj:
        return fileobj.read().splitlines()


def file_to_list(path: Path) -> list:
    with open(path, 'r') as fileobj:
        lst_data = fileobj.read().splitlines()
    lst_data = [data for data in lst_data if data]
    return lst_data
