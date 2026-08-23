def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print(f"Error: invalid Numeric Input \n")
        except IndexError:
            print("Invalid Expense Number", end="\n")
    return wrapper