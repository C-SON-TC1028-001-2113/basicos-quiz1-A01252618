import math
def main():
    #escribe tu código abajo de esta línea
    print("punto inicial:")
    x1=int(input("x1= "))
    y1=int(input("y1= "))
    
    print("punto final:")
    x2=int(input("x2= "))
    y2=int(input("y2= "))
    
    distancia= float(math.sqrt((x2-x1)**2 +(y2-y1)**2))
    distancia= round(distancia,2)
    print("distancia= " ,distancia)



if __name__ == '__main__':
    main()
