# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for key, value in phone_numbers.items():
#   print("{}: {}".format(key, value))

# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for values in phone_numbers.values():
#    new_number = values.replace("+", "00")
#    print(new_number)


# def repeat_input(user_input):
#    capitalized = str(user_input).capitalize()
#    if str(user_input).startswith(("how", "what", "why")):
#        return "{}? ".format(capitalized)
#    else:
#        return "{}.".format(capitalized)

# phrases = []
# while True:
#    user_input = input("Say something: ")
#    if user_input == "\end":
#        break
#    else:
#        phrases.append(repeat_input(user_input))

# print(" ".join(phrases))

# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

# temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(new_temps)

# array = []

# def only_nums(array):
#    new_array = [num for num in array if num != str(num) and num > 0]
#    return new_array

# temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

temps = [99, 'no data', 95, 94, 'no data']
def replace_data(array):
    new_data = [0 if i == 'no data' else i for i in array]
    return new_data

print(replace_data(temps))

def sum_of_list(array):
    new_data = sum([float(num) for num in array])
    return new_data