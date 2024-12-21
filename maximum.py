string = input("Введите строку (Для выхода нажмите enter) ")
string_array = []

while string != "" :
    string = input("Введите строку (Для выхода нажмите enter) ")
    string_array.append(string)

print(max(string_array))
