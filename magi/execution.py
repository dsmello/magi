import os
from magi.nodesolver import  nodesolver
from magi.readfiles import read_yaml_files
from magi.rest_engine import rest_call

def run(folder_path:str=None)->None:

    YAMLS_ON_FOLDER : dict = read_yaml_files(folder_path)

    for yaml in YAMLS_ON_FOLDER:
        request_list : list = nodesolver(YAMLS_ON_FOLDER[yaml])
        for rest_request in request_list:
            rest_call(**rest_request)

