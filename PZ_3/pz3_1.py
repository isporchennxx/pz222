#  Даны три целых числа : А,В,С.Проверить истиность высказывания:"Хотя бы одно из чисел А,В,С Положительное"
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))

if A > 0 or B > 0 or C > 0:
    print("Высказывание истинно: Хотя бы одно из чисел А, В, С положительное")
else:
    print("Высказывание ложно: Ни одно из чисел А, В, С не является положительным")