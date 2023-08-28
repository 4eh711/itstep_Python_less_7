def cheker(function, *args, **kwargs):
    try:
        result = function(*args, **kwargs)
    except Exception as exc:
        print(f"We have problems {exc}")
    else:
        print(f"No problems. Result - {result}")

def calculate(expression):
    return eval(expression)

cheker(calculate, "2+2")
