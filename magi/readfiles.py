import os
import yaml
import logging


errors: dict = {
    'bad_folder_path'   :   'The path of folder not is a directory.',
    'bad_path_not_exist':   'The path not exist.',
    'empty_folder'      :   'The folder are empty.'
}


def hello() -> str:
    return "world"


def is_folder( folder_path: str, error_msg: str = errors['bad_folder_path']) -> str:
    if not os.path.isdir(folder_path):
        logging.error(error_msg)
        raise IOError(error_msg)
    return folder_path


def __clean_str__(original_str: str, bad_str: str, startswith: str = '/') -> str:
    result: str = original_str.replace(bad_str, '')
    
    if result.startswith(startswith):
        return result[1:]
    return result


def list_files(filepath: str, prefix: str = '') -> dict:
    is_folder(filepath)

    files: dict = {}

    for file in os.listdir(filepath):
        path: str = f"{filepath}/{file}"
        if os.path.isfile(path):
            files[f'{prefix}{__clean_str__(path, filepath)}'] = path

        if os.path.isdir(path):
            files = {**files, **list_files(path, prefix=f'{file}/')}

    return files


def empty_folder(folder_path: str, error_msg: str = errors['empty_folder']) -> bool:
    if not list_files(folder_path):
        logging.warning(error_msg)
        return False
    return True


def load_file(filepath: str) -> str:
    file_data: str
    with open(filepath, 'r') as data:
        file_data = data.read()
    return file_data


def __read_yaml__(filepath: str) -> dict:
    content: str = load_file(filepath)
    return dict(yaml.load(content, Loader=yaml.FullLoader))


def read_yaml_files(filepath: str, sufix: str = '.yaml') -> dict:
    files: dict = list_files(filepath)
    result: dict = {}
    for key in files.keys():
        if key.endswith(sufix):
            result[__clean_str__(key, sufix)] = __read_yaml__(files[key])
    return result

