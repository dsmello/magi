import logging
from magi.sys_env import replace_by_sys_variables 



def __get_basic_info__(raw_input:dict, sys_env_replacer:bool=True) -> dict: 
    metadata : dict = raw_input.get("metadata")
    if sys_env_replacer:
        replace_by_sys_variables(metadata)
    return metadata


def __metadata_auth__(raw_metadata_auth_input:dict) -> dict:
    auth_input : dict = raw_metadata_auth_input

    if auth_input.get("auth"):
        auth_input = auth_input.get("auth")

    # basic authentication
    if auth_input.get("basic"):
        basic_auth : dict = auth_input.get("basic")
        return {"auth":(basic_auth.get("user"), basic_auth.get("password"))}
    
    return {}


def __metadata__(raw_input:dict) -> dict: 
    metadata: dict = __get_basic_info__(raw_input)

    result : dict = {}

    if metadata.get("url"):
        result["url"] = metadata.get("url")

    if metadata.get("auth"):
        result = dict(**result, **__metadata_auth__(metadata))
    
    return result


def __get_requests__(raw_input:dict) -> list : 
    return raw_input.get("requests")


def __url__(url_base: str, url_endpoint: str) -> str:
    base : str = url_base
    endpoint : str = url_endpoint

    if base[-1] == "/":
        base = base[:-1]
    
    if endpoint[0] == "/":
        endpoint = endpoint[1:]
    
    return f"{base}/{endpoint}"

def __inject_basic_info__(metadata_input:dict, raw_request_input:dict) -> dict:
    

    result : dict = {}
    for node_name in raw_request_input:
        request_list : list = []
        for request_item in raw_request_input[node_name]:
            metadata: dict = metadata_input.copy()
            request_item_copy: dict = request_item.copy()
            request : dict = {}
            if metadata.get("url") and request_item_copy.get("url"):
                request["url"] = __url__(metadata.get("url"), request_item_copy.get("url"))
                metadata.pop("url")
                request_item_copy.pop("url")

            request = dict(**request, **metadata, **request_item_copy)

            if not request.get("method"):
                request["method"] = "GET"
            else:
                request["method"] = request.get("method").upper()
            request_list.append(request)
        result[node_name] = request_list
    return result
            

# TODO: Implements the method sort
def __sort_requests__(raw_input:dict) -> list : 
    result : list = []
    for node in raw_input:
        for request in raw_input[node]:
            result.append(request)
    return result


def nodesolver(input_data: dict) -> list:
    metadata: dict = __metadata__(input_data)
    request_dict :dict = __inject_basic_info__(metadata_input=metadata, raw_request_input=__get_requests__(input_data))

    return __sort_requests__(request_dict)