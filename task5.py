# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Не думаю что это правильное решение, получается постоянно истина, но может так:

def enterXYZ(x):
    xyz = ['X','Y','Z']
    num = []
    for i in range(x):
        num.append(input(f'Введите значение предикат {xyz[i]}: '))
    return num


def checkCondition(x):
    a = not (x[0] or x[1] or x[2])
    b = not x[0] and not x[1] and not x[2]

    return a==b


if checkCondition(enterXYZ(3)) == True:
    print('Это истинное утверждение')
else:
    print('Это ложное утверждение')