from collections import Counter, defaultdict
from typing import NamedTuple
from datetime import date, datetime
import csv

Reserva = NamedTuple("Reserva", 
                     [("nombre", str),
                      ("dni", str),
                      ("fecha_entrada", date),
                      ("fecha_salida", date),
                      ("tipo_habitacion", str),
                      ("num_personas", int),
                      ("precio_noche", float),
                      ("servicios_adicionales", list[str])
                    ])

def lee_reservas(ruta_fichero: str) -> list[Reserva]:
    with open(ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=",")
        next(lector)
        lista_reservas = []
        for (nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_str) in lector:
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d")
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            if servicios_str == "":
                servicios_adicionales = []
            else:
                servicios_adicionales = [s.strip() for s in servicios_str.split(",")]
            reservas = Reserva(nombre,dni,fecha_entrada,fecha_salida,tipo_habitacion,num_personas,precio_noche,servicios_adicionales)
            lista_reservas.append(reservas)
    return lista_reservas

def total_facturado(reservas: list[Reserva], 
                    fecha_ini: date | None = None, 
                    fecha_fin: date | None = None) -> float:
    total = 0
    for reserva in reservas:
        if (fecha_ini <= reserva.fecha_entrada.date() <= fecha_fin):
            dias_totales = (reserva.fecha_salida - reserva.fecha_entrada).days
            total += (dias_totales * reserva.precio_noche)
    return total

def reservas_mas_largas(reservas: list[Reserva], n: int = 3) -> list[tuple[str, date]]:
    ordenadas = sorted(reservas, key=dias, reverse=True)
    return [(r.nombre, r.fecha_entrada) for r in ordenadas[:n]]

def dias(reserva:Reserva) -> int:
    return (reserva.fecha_salida - reserva.fecha_entrada).days

def cliente_mayor_facturacion(reservas: list[Reserva], servicios: set[str] | None = None) -> tuple[str, float]:
    
    facturacion_por_cliente = defaultdict(float)
    for reserva in reservas:
        cumple_el_filtro = (servicios is None) or any(s in reserva.servicios_adicionales for s in servicios)
        if cumple_el_filtro:
            facturacion_por_cliente[reserva.dni] += total_facturacion(reserva)
    if not facturacion_por_cliente:
        return ("", 0.0)
    return max(facturacion_por_cliente.items(), key=lambda item: item[1])
        
def total_facturacion(reserva:Reserva) -> float:
    return reserva.precio_noche * dias(reserva)