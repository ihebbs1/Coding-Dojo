num1 = 42 #        - Numbers
num2 = 2.3 #        - Numbers
boolean = True #Boolean
string = 'Hello World' #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #tuples
print(pizza_toppings[1]) #sausage
pizza_toppings.append('Mushrooms')#['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives', 'Mushrooms']
print(person['name'])#john
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])#banana

if num1 > 45:
    print("It's greater")#false
else:
    print("It's lower")#true

if len(string) < 5:
    print("It's a short word!")#false
elif len(string) > 15:
    print("It's a long word!")#false
else:
    print("Just right!")#true

for x in range(5):
    print(x)#0,1,2,3,4
for x in range(2,5):
    print(x)#2,3,4
for x in range(2,10,3):
    print(x)#2,5,8
x = 0
np=200
while(x < np):
    print(x)#0,1,2,3,4
    x += 1#1,2,3

pizza_toppings.pop()#['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese']
pizza_toppings.pop(1)#['Pepperoni', 'Jalepenos', 'Cheese', 'Olives']

print(person)#{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person.pop('eye_color')#{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person)#{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)

