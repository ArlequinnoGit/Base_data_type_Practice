#1st Создайте переменную my_string
#и присвойте ей значение строки с произвольным текстом
# (функция input()).
my_string = input()

#2nd Вывести количество символов введённого текста
#Использовал функцию len()
print(len(my_string))

#3rd Работа с методами строк
#Выведите строку my_string в верхнем регистре.
print(my_string.upper())

#Выведите строку my_string в нижнем регистре.
print(my_string.lower())

#Измените строку my_string, удалив все пробелы.
print(my_string.replace(" " ,""))
#Выведите первый символ строки my_string.
print(my_string[0:1])
#Выведите последний символ строки my_string.
print(my_string[-1:])