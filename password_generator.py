
#0 -> '00'
#0 -> '01'

alphabet = '0123456789qwertyuiopasdfghjklzxcvbnm'

lenght = 0
state = 0
base = len(alphabet)

while True:
    password = ''
    temp_state = state
    while temp_state >0:
        ceil = temp_state // base
        rest = temp_state % base
        password = alphabet[rest] + password
        temp_state = ceil

    password = alphabet[0] * (lenght - len(password)) + password

    print(state, password)

    state +=1
    if password == alphabet[-1]*lenght:
        lenght +=1
        state = 0

        if len(password) ==3:
                break