# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("Error!!! Division by zero is not possible.'ZeroDivisionError Block")
# except ValueError:
#     print("Error!!! Invalid number given.'Value Error Block")
# else:
#     print("No exceptions occured.'Else Block")
# finally:
#     print("Finally block executed")



# try:
#     num = int('Saurav')
# except ValueError as p:
#     print("Can not store string type in int", p)



# x = 20
# if x > 0:
#     print("Stored the amout: ", x)
# else:
#     raise Exception("Sorry, number less then or equal to zero are not allowed")


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise MyCustomException("Age can not be a negative number")
except MyCustomException as e:
    print("Custom Exception:", e.message)