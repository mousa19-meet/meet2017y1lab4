speed = input(' what is the speed?')
bday = False

if bday:
    if int(speed) < 36:
        print("no ticket")
    elif int(speed) > 36 and int(speed) < 56:
        print('smal ticket')
    elif int(speed) > 56:
        print ('big ticket')
else:
    if int(speed) < 31:
        print('no ticket')
    elif int(speed) > 30 and int(speed) < 51:
        print('small ticket')
    elif int(speed) > 51:
        print("big ticket")
