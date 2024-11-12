from typing import Optional

# str_to_float
########################################################################################################################
# the str_to_float function will use a try except block to handle value errors if a non float type value is passed to
# the built-in float funciton

def str_to_float(input_string: str) -> Optional[float]:
    try:
        result =  float(input_string)
    except ValueError:
        return None
    return result