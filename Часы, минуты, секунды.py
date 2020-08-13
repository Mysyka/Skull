
H = 'час'
M = 'минут'
S = 'секунд'

a=int(input('Введите количество секунд:'))
h=a//3600
m=(a//60)%60
s=a%60
if 2 <= h <= 4:
    H = H + 'а'
if h >= 5 or h == 0:
    H = H+ 'ов'
if m == 1:
    M = M + 'а'
if 2 <= m <= 4:
    M = M + 'ы'
if s == 1:
    S = S + 'а'
if 2 <= s <= 4:
    S = S + 'ы'

if h == 0:
    print(m, M, s, S);

if m == 0:
    print(h, H, s, S);

if s == 0:
    print(h, H, m, M);

