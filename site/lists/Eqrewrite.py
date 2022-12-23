### Attempt to rewrite as a function all variables. Only works for +-*/ ###

def get_all_variables_from_equation(equation, ignore):
    variables = []
    for char in equation:
        if str(char).isalpha() and char not in variables and char != ignore:
            variables.append(char)
    return variables

possible_formulas = {}
dummy = input("Enter your equation: ")
left_side = dummy.strip().split("=")[0].strip()
right_side = dummy.strip().split("=")[1].strip()
possible_formulas[left_side] = right_side

other_variables = get_all_variables_from_equation(dummy, left_side)

for variable in other_variables:
    posibble = right_side.split(variable)
    temp = ""
    for value in posibble:
        if len(value.strip()) > 1:
            if value.strip()[0] not in "/*-+":
                if value.strip().endswith("/"):
                    if left_side in temp:
                        temp = value.strip() + temp
                    else:
                        temp = temp + value.strip() + left_side
                elif value.strip().endswith("*"):
                    replaced = "/" + value.strip()[:len(value.strip()) - 1]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
                elif value.strip().endswith("+"):
                    replaced = "-" + value.strip()[:len(value.strip()) - 1]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
                elif value.strip().endswith("-"):
                    replaced = "+" + value.strip()[:len(value.strip()) - 1]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
            elif value.strip()[0] in "/*-+":
                if value.strip().startswith("/"):
                    replaced = "*" + value.strip()[1:]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
                elif value.strip().startswith("*"):
                    replaced = "/" + value.strip()[1:]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
                elif value.strip().startswith("+"):
                    replaced = "-" + value.strip()[1:]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
                elif value.strip().startswith("-"):
                    replaced = "+" + value.strip()[1:]
                    if left_side in temp:
                        temp += replaced
                    else:
                        temp += left_side + replaced
        else:
            temp+= "/" + value.strip()

    if temp[0] in "/*+-":
        temp = temp[1:]
    elif temp[len(temp)-1] in "/*+-":
        temp = temp[:len(temp)-1]
    possible_formulas[variable] = temp

print("the possibilites are = ")
for key in possible_formulas.keys():
    print(f'{key}={possible_formulas[key]}')
