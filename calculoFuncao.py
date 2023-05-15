
def calculo_funcao(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        xV = -b / (2 * a)
        print(f"O x do verticie é {xV}")
        yV = -delta / (4 * a)
        print(f"O y do verticie é {yV}")
    else:
        x1 = (-b + delta **0.5)/ (2 * a)
        x2 = (-b - delta **0.5)/ (2 * a)
        print(f"A primeira raiz vale {x1} a segunda vale {x2}")
        xV = -b / (2 * a)
        print(f"O x do verticie é {xV}")
        yV = -delta / (4 * a)
        print(f"O y do verticie é {yV}")


while True: 
    a = int(input("Informe o (a): "))
    b = int(input("Informe o (b): "))
    c = int(input("Informe o (c): "))
    calculo_funcao(a, b, c)




        