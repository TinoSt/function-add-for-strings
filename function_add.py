
string1 = "Was ein schöner Tag"
string2 = "das noch werden kann."


def add(x, y):
    if isinstance(x, str) and isinstance(y, str):
        generate_list = [x, y]
        added_string = " ".join(generate_list)
        return added_string
    else:
        print("Die Funktion add() benötigt Variablen "
              "vom Datentyp str...")


result = add(string1, string2)
print(result)



