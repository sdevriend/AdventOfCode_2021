from pathlib import Path


def file_to_list(path: Path) -> list:
    with open(path, 'r') as fileobj:
        lst_data = fileobj.read().splitlines()
    lst_data = [data for data in lst_data if data]
    return lst_data
