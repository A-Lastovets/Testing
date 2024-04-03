import time
while True:
    a = input('Enter how many liters per 100 km your car needs: \n')
    try:
        n = float(a)
        if n > 0:
            break
        else:
            print('Invalid number\n')
    except:
        if a.isalpha():
            print("Letters entered\n")
        else:
            print("Unaccepted characters entered\n")
###########################################################################
while True:
    b = input('Enter the price per liter, zl: \n')
    try:
        n = float(b)
        if n > 0:
            break
        else:
            print('Invalid number\n')
    except:
        if b.isalpha():
            print("Letters entered\n")
        else:
            print("Unaccepted characters entered\n")
############################################################################
while True:
    c = input('How many km do you have to drive / have already driven: \n')
    try:
        n = float(c)
        if n > 0:
            break
        else:
            print('Invalid number\n')
    except:
        if c.isalpha():
            print("Letters entered\n")
        else:
            print("Unaccepted characters entered\n")
#############################################################################
km_1 = float(b) * float(a)/100
print('Price for 1 km: ', round(km_1, 2))
km_all = km_1 * float(c)
print('The price will be for kilometers traveled: ', round(km_all, 2))

time.sleep(3)