def countdown(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result

countdown_list = countdown(5)
print(countdown_list)

def print_and_return(numbers):
    if len(numbers) >= 2:
        print(numbers[0])
    return numbers[1]

result = print_and_return([1, 2])
print(result)


def first_plus_length(my_list):
    if my_list:
        return my_list[0] + len(my_list)

result = first_plus_length([1, 2, 3, 4, 5])
print(result)


def values_greater_than_second(my_list):
    
    if len(my_list) < 2:
        return False
    second_value = my_list[1]

    new_list = []
    for value in my_list:
        if value > second_value:
            new_list.append(value)

    print(len(new_list))
    
    return new_list

result = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result)

result2 = values_greater_than_second([3])
print(result2)




def length_and_value(size, value):
    new_list = [value] * size

    return new_list

result1 = length_and_value(4, 7)

print("Result 1:", result1)

result2 = length_and_value(6, 2)

print("Result 2:", result2)


