import requests
import logging


def rest_call(rest_engine = requests.request, **kwargs) -> int:
    call : requests.Response = rest_engine(**kwargs)
    logging.info(msg=f"REST_CALL: {kwargs['url']} -> method : {kwargs['method']} -> status_code : {call.status_code}")
    logging.debug(msg=f"JSON : {kwargs['url']}")
    print(f"REST_CALL: {kwargs['url']} -> method : {kwargs['method']} -> status_code : {call.status_code}")
    return call.status_code