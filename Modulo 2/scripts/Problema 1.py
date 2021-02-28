while True:
    try:
        altura = int(input("Digite altura (1-8): "))
        if altura<=0 or altura>=9:
            print("Por favor, digite un número válido")
            altura = int(input("Digite altura (1-8): "))
    except:
        print("Digite un número válido")
    else:
        break

n = altura

for i in range(altura):
    print(" "*(n-1) + "#"*(i+1))
    n -= 1