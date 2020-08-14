H = 'час'
M = 'минут'
S = 'секунд'

#перевод секунд в минуты и часы
a = int(input('Введите количество секунд:'))
h = a//3600
m = (a//60)%60
s = a%60

#окончания
if 2 <= h <= 4:
    H = H + 'а'
if h >= 5 or h == 0:
    H = H + 'ов'
if m == 1:
    M = M + 'а'
if 2 <= m <= 4:
    M = M + 'ы'
if s == 1:
    S = S + 'а'
if 2 <= s <= 4:
    S = S + 'ы'
print(h, H, m, M, s, S)
#проверка на нули/ но тогда вывод работает криво
#if h == 0:
#    print(m, M, s, S)
#else:
#    print(h, H, m, M, s, S)
#if m == 0:
#    print(h, H, s, S)
#else:
#    print(h, H, m, M, s, S)
#if s == 0:
#    print(h, H, m, M)
#else:
#    print(h, H, m, M, s, S)
