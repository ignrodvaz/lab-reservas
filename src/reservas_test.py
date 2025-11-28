from reservas import *

if __name__ == "__main__":
    # #EJERCICO 1
    # print("Test lee_reservas")
    datos = lee_reservas("./data/reservas.csv")
    # print(f"Total reservas: {len(datos)}")
    # print("Mostrando los 3 primeros:")
    # for dato in datos[:3]:
    #     print(dato)
        
    # #EJERCICIO 2
    # print("Test total_facturado")
    # # fecha_ini = date(2022, 2, 1)
    # # fecha_fin = date(2022, 2, 28)
    # # print(fecha_ini, fecha_fin)
    # print(total_facturado(datos, fecha_ini = date(2022, 2, 1), fecha_fin = date(2022, 2, 28)))
    
    #EJERCICIO 3
    print("Test reservas más largas")
    print(reservas_mas_largas(datos, n=3))
    
    #EJERCICIO 4
    print("Test cliente mayor facturacion")
    print(cliente_mayor_facturacion(datos))