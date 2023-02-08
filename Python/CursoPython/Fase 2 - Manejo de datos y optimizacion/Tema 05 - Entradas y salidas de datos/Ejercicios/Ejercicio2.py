import sys
print(sys.argv)


if len(sys.argv) == 3:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    if (num1 >= 0 and num1 <= 9 and num2 >= 0 and num2 <= 9):
        print()

        for x in range(num1):
            print()
            for j in range(num2):
                print(" * ", end='')



    else:
        print('El numero debe estar entre 0 y 9')    

else:
    print('Debes introducir todos los datos en los argumentos')