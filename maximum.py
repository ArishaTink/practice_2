count = int(input("Введите кол-во строк в массиве "))
string = input("Введите строку (Для выхода нажмите enter) ")
string_array = []

for i in range(1,count):
    string = input("Введите строку (Для выхода нажмите enter) ")
    string_array.append(string)

print(min(string_array))
