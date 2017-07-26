strawberries = 70
is_weekend = True

if is_weekend:
    if int(strawberries) > 39:
        print ('FUN')
    else:
        print('not fun')
else:
    if int(strawberries) > 39 and int(strawberries) < 61:
        print('not fun')
    else:
        print('NOT FUN')
