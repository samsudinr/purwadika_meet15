def getHello(nama):
  print("hello " + nama)

alpha = input("Masukan Nama")
getHello(alpha)
print('The code is done')


# basic function
def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'