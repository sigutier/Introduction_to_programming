def ask_int(ask_message):
    while True:
        str_number = input(ask_message)
        try:
            number = int(str_number)
        except:
            print("Debes introducir un número entero.")
            continue
        if number < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    return number

def ask_float(ask_message):
    while True:
        str_number = input(ask_message)
        try:
            number = float(str_number)
        except:
            print("Debes introducir un número.")
            continue
        if number < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    return number
