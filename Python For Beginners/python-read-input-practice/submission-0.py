def add_two_numbers() -> int:
    inputs = input()

    split_inputs = inputs.split(",")
    listed_numbers = []

    for item in split_inputs:
        listed_numbers.append(int(item))

    first = listed_numbers[0]
    second = listed_numbers[1]

    return first + second



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
