#Little wolf calculator v0.1
from colorama import init
from colorama import Fore, Back, Style #Модуль цвета
init()
print( Back.BLACK )
print( Fore.RED )
print("Little wolf calculator v0.1")
print( Back.GREEN )
print( Fore.BLACK )
what = input("Необходимая опирация? (+,-,*,/): ")
print( Back.CYAN )
print( Fore.BLACK )
a = float(input("Первое число: "))
if a > int(50) :
    print("Were big number")

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print( Back.YELLOW )
print( Fore.BLACK )
if what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	c = a - b
	print("Результат: " + str(c))

elif what == "*":
    c = a * b
    print("Результат: " + str(c))

elif what == "/":
	c = a / b
	print("Результат: " + str(c))


else:
    print("Неверная опирация!")
