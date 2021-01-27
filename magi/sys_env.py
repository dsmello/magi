import os

def replace_by_sys_variables(metadata_raw:dict, sys_var_prefix:str="MAGI_YAML") -> None:
    """
    This method change the input object in memory.
    """

    metadata: dict = metadata_raw

    for key in metadata:
        sys_var: str = f"{sys_var_prefix}_{str(key).upper()}"
        if isinstance(metadata[key], dict):
            replace_by_sys_variables(metadata_raw=metadata[key], sys_var_prefix=sys_var)
        
        elif os.getenv(sys_var):
            metadata[key] = os.getenv(sys_var)

