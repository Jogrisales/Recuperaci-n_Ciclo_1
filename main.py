#Funcion Principal para el desarrollo ambos talleres.
#Esta función sólo llamará a los talleres de las hojas de los mismos.
import os
print("_"*37)
print("\nPROGRAMA  PARA TALLER DE RECUPERACIÓN\n")
#Crear el programa principal.
import solucionTaller as Taller

print("="*37)
print("Menu Programas Taller Recuperación.\n\t1.Programa de informacion de Pasajeros.\n")
opcion = int(input("Digite el programa: "))
if opcion == 1:
  Taller.menu_iter()
else:
    print("Opción no existente.")