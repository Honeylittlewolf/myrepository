#Little wolf calculator v0.1
from colorama import init
from colorama import Fore, Back, Style #Модуль цвета 
init()
print( Back.GREEN )
print( Fore.BLACK )
print("Little wolf calculator v0.1")
what = input("Необходимая опирация? (+,-): ")
print( Back.CYAN )
print( Fore.BLACK )
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

else:
    print("Неверная опирация!")
