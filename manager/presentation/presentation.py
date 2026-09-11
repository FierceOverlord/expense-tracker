from utilities.resultFormat import print_format


def print_dictionary(data):
    for key,value in data.items():
        print(f"{key}: {value}")



@print_format
def display_expense(result):
    return result


def display_result(result):
    if result is None:
        return 

    if isinstance(result, list):
        if not result:
            print("No expense found.")
            return 

        display_expense(result)

    elif isinstance(result, dict):
        print_dictionary(result)

    else:
        display_expense(result)


