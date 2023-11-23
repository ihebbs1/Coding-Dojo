for i in range(0, 151):
    print(i)

# Multopes of 5 to 1000

print(f"The multiples of 5 from 5 to 1000 are:")
for i in range(5, 1000):
    if i % 5 == 0:
        print(i)

# # counting the dojo

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# #whoa. That Sucker's Huge

sum_of_odd_numbers = 0
for number in range(0, 500001):
    if number%2==1:
        sum_of_odd_numbers+=number
print(sum_of_odd_numbers)

# #Countdown by Fours

starting_number = 2018
for number in range(starting_number, 0, -4):
    print(number)

# #flexible counter

lowNum = 5
highNum = 20
mult = 4
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

