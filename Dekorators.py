def cheker(function):
    def cheker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result - {result}")
    return  cheker

def calculate(expression):
    return eval(expression)

calculate = cheker(calculate)
calculate("2+2")
