first = input('Введите первое число ')
second = input('Введите второе число ')
third = input('Введите третье число ')
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

