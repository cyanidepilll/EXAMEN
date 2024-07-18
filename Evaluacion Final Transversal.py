#Evaluacion Final Transversal
import easygui
import random
import csv
import math


titulo= "Reportes de sueldos"


workers= {"Juan Pérez:",
"María García:",
"Carlos López:",
"Ana Martínez:",
"Pedro Rodríguez:",
"Laura Hernández:",
"Miguel Sánchez:",
"Isabel Gómez:",
"Francisco Díaz:",
"Elena Fernández:"}

limite1= []
limite2= []
limite3= []
reporte= []


trabajadores_sueldos= {}




def asignar(workers, trabajadores_sueldos):
    trabajadores_sueldos={worker: random.randint(300000, 2500000) for worker in workers}
    easygui.msgbox(f"Sueldos generados", titulo)
    for worker, sueldo in trabajadores_sueldos.items():
        if 800000 >= sueldo:
            limite1.append({worker: sueldo})
        if sueldo >= 2000000:
            limite3.append({worker: sueldo})
        if sueldo >= 800000 and 2000000>= sueldo:
            limite2.append({worker: sueldo})

    print(limite1)
    print(limite2)
    print(limite3)


def clasificar(limite1, limite2, limite3, trabajadores_sueldos):
    sueldos= (f"Sueldos menores a 800000: {limite1}. TOTAL: {len(limite1)}",
              f"Sueldos entre 800000 y 2000000: {limite2}. TOTAL: {len(limite2)}",
              f"Sueldos mayores a 2000000: {limite3}. TOTAL: {len(limite3)}")
    easygui.msgbox(sueldos, titulo) 



def estadísticas(trabajadores_sueldos):
    estadistica= (f"Sueldo más alto",
                  f"Sueldo más bajo"
                  f"Promedio de sueldos"
                  f"Media Geométrica")
    easygui.msgbox()


def reporte(limite1, limite2, limite3, reporte):
    print(limite1)
    limite1= {}
    for worker, sueldo in limite1.items():
        salud= sueldo*0.07
        afp= sueldo*0.12
        liquido= sueldo-afp-salud
    todos= sueldo, salud, afp, liquido
    reporte.append({worker:todos})
    print(reporte)






menu= ["1. Asignar sueldos aleatorios", 
"2. Clasificar Sueldos",
"3. Ver estadísticas", 
"4. Reporte de sueldos",
"5. Salir del Programa"]


while True:
    choice= easygui.choicebox("Bienvenido, seleccione una opción", titulo, menu)
    if choice == "1. Asignar sueldos aleatorios":
        asignar(workers, trabajadores_sueldos)
    if choice == "2. Clasificar Sueldos":
        clasificar(limite1, limite2, limite3, trabajadores_sueldos)
    if choice == "3. Ver estadísticas":
        print("a")
    if choice == "4. Reporte de sueldos":
        reporte(limite1, limite2, limite3, reporte)
    if choice == "5. Salir del Programa":
        easygui.msgbox("Cerrando. Desarrollado por Sofía Mayorga RUT 21.821.404-5")
        break
