#identify how many letters are in the given string
#divide the length by two

def middle_letter(string_variable):
    if len(string_variable)%2 == 0:
        return ""
    elif len(string_variable)%2 == 1:
        string_variable_list = string_variable.split()
        return string_variable_list[len(string_variable_list)//2]
    else:
        print("I do not understand")

middle_letter("how")
