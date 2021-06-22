import math

# константы
M = 2150
m = 1000
g = 1.62
a_max = 29.43 # перегрузка
v_r = 3660 # скорость истечение газа
v_y_max = 3 # макс. вертикальная скорость при посадке
v_x_max = 1 # макс. горизонтальная скорость при посадке
l = 250000 # необходимая дальность


# данные моего варианта
h_0 = float(input('h_0 = ')) # начальная высота
h_k = float(input('h_k = ')) # конечная высота

v_x = 0
v_y = 0
y = h_0
x = 0
t = 0
flag = 0

# 1 этап
while x + v_x * ((v_y)/(g)) < (l)/(2): # задача симметричная, т.е условие на достижение середины пути во горизонтали
    alpha = 45 # задали угол
    rada = (alpha * math.pi)/(180)
    d_m = 5 # задали расход
    a = -g * math.sin(rada) + (v_r * d_m)/(M)
    v_x += a * math.cos(rada) * 0.1
    v_y += a * math.sin(rada) * 0.1
    x += v_x * 0.1
    y += v_y * 0.1
    m -= ((d_m) / 10)
    M -= - ((d_m)/10)
    if m < 0 or a > a_max:
        flag = 1
    print(v_x, v_y, x, y, alpha, m, t)
    t += 0.1

#  2 этап
# Выключили двигатель, далее инерция, т.е горизонтальная скорость сохраняется
h = y
while y > h - 0.1: # пока не окажется на той же высоте, что и до выключения двигателя
    if y < h_k:
        flag = 1
    v_y -= g * 0.1
    y += v_y * 0.1
    x += v_x * 0.1
    print(v_x, v_y, x, y, alpha, m, t)
    t += 0.1

v_y = math.fabs(v_y)

# 3 этап
phi = math.atan((y - h_k)/(l - x))
radp = (phi * math.pi)/(180)
while y > h_0:
    if y < (v_y**2)/(2 * a_max * math.sin(radp)) + h_k:  # прекращение цикла по достижении критической высоты, начиная с которой начнется гашение скорости до посадочной
        break
    alpha = 45  # задали угол
    rada = (alpha * math.pi) / (180)
    d_m = 5  # задали расход
    a = -g * math.sin(rada) + (v_r * d_m) / (M)
    v_x -= a * math.cos(rada) * 0.1
    v_y -= a * math.sin(rada) * 0.1
    x += v_x * 0.1
    y -= v_y * 0.1
    m -= ((d_m) / 10)
    M -= - ((d_m) / 10)
    if m < 0 or y < h_k or a > a_max:
        flag = 1
    print(v_x, v_y, x, y, alpha, m, t)
    t += 0.1

# 4 этап
phi = math.atan((y - h_k)/(l - x))
radp = (phi * math.pi)/(180)
while y > h_k + 0.00001 or y < h_k - 0.00001:  # +-0.00001 для того, чтобы цикл закончился, в противном случае он не остановится (грубо говоря здесь указываем точность)
    a_x = (v_x**2)/(2 * (l - x))
    a_y = (v_y**2)/(2 * (y-h_k))
    a = math.sqrt(a_x**2 + a_y**2)
    d_m = (M * a + M * g * math.sin(radp))/(v_r)
    v_x -= a_x * 0.1
    v_y -= a_y * 0.1
    x += v_x * 0.1
    y -= v_y * 0.1
    m -= ((d_m) / 10)
    M -= - ((d_m) / 10)
    if m < 0 or y < h_k or a > a_max:
        flag = 1
    print(v_x, v_y, x, y, alpha, m, t)
    t += 0.1

if v_x > v_x_max or v_y > v_y_max:
    flag = 1

if flag == 1:
    print('')
    print('FAIL')
else:
    print('')
    print('SUCCESS')