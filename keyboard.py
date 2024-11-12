import convert

def gather_numbers():
    user_input = ''
    listed_inputs = []
    while user_input.strip() != 'done':
        user_input = input("type a number:")
        if type(convert.str_to_float(user_input)) == float:
            listed_inputs.append(convert.str_to_float(user_input))
    return listed_inputs



print (gather_numbers())