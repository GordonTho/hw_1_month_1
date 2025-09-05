# def calc ():
#     num1 = int(input("Введите первое число"))
#     num2 = int(input("Введите второе число"))
#     print(num1 + num2)
# calc()

# def calc (num1, num2):
#     print(num1 + num2)
# calc(10, 20)

# def full_name(name: str):
#     print("Здраствуйте", name)

# full_name("Joe")

# def add(num1: int, num2: int):
#     print(num1 + num2)

# def sub(num1: int, num2: int):
#     print(num1 - num2)

# def mult(num1: int, num2: int):
#     print(num1 * num2)

# def div(num1: int, num2: int):
#     print(num1 / num2)

# def calculator(num1: int, operator: str, num2: int):
#     if operator == "+":
#         add(num1,num2)
#     elif operator == "-":
#         sub(num1,num2)
#     elif operator == "*":
#         sub(num1,num2)
#     elif operator == "/":
#         sub(num1,num2)
#     else:
#         print("Ошибка")


numbers = [10, 20, 1, 5, 3, 44]
tup_numbers = (2, 3, 123, 42, 45, 12, 54)

def list_chet(lst_num: list) -> str:
    for num in lst_num:
        if num % 2 == 0:
            print(num, "Чет")
        else:
            print(num, "Нечет")

list_chet(numbers)
list_chet(tup_numbers)

def hello():
    return"hello"

print(hello()) 


