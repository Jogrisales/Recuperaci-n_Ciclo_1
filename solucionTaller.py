import os
pasajeros = []
lista_pasajeros = [("Jorge Grisales",75146770,"Pereira"), ("Samuel Grisales",1085719512,"Caertago"), ("Brenda Cabrera",1088240004,"Dosquebradas"), ("Sofia Grisales",1088650147,"Cali")]
for i in lista_pasajeros:
  pasajeros.append(i) 
def leer_archivos():
  #Para valores departamentos
  lista_departamentos = []
  departamentos = open("Departamentos_Capitales.csv","r")
  for i in departamentos:
    i = i.replace("\n", "")
    i = i.split(",")
    lista_departamentos.append(i)
  departamentos.close()  
  ld_f = len(lista_departamentos)
  departamentosCapitales = []
  for i in range(0,ld_f):
    pos1 = lista_departamentos[i][0]
    pos2 = lista_departamentos[i][1]
    departamentosCapitales.append((pos1,pos2))
  return departamentosCapitales

# Función agregar pasajeros, usando tupla.
def ingrearPasajero():
  os.system("clear")
  print("Se solicitarán: \n1.Nombre del pasajero(nombre apellido)\n2.Documento de identidad del pasajero.\n3.Ciudad de destino.\n")
  nombre = str(input("Digite nombre pasajero:"))
  identificacion = int(input("Digite documento identidad pasajero:"))
  ciudad = str(input("Digite ciudad de destino:"))
  if nombre.count(" ") == 1:
    nombre_viajero = nombre
    if identificacion > 0 and identificacion < 99999999999999:
      identificacion_viajero = identificacion
      if ciudad.count(" ") <= 1 and ciudad.isdigit() == False:
        ciudad_viajero = ciudad
        pasajeros.append((nombre_viajero,identificacion_viajero,ciudad_viajero))
        # print(lista_pasajeros)
        print("Desea agregar otro pasajero(Si/No)")
        ele = 0
        ele = str(input())
        if ele == "Si" or ele == "si":
          ingrearPasajero()
        if ele == "No" or ele == "no":
          return pasajeros
        else:
          print("Eleccion no valida, presione cualquier tecla para continuar.")
          input()
          ingrearPasajero()
      else:
        print("Ciudad no válida, vuelva a ingresar datos, presione cualquier tecla para continuar.")
        input()
        ingrearPasajero()
    else:
      print("Documento no válido, vuelva a ingresar datos, presione cualquier tecla para continuar")
      input()
      ingrearPasajero()
  else:
    print("Nombre no válido, vuelva a ingresar datos, presione cualquier tecla para continuar")
    input()
    ingrearPasajero()

def verificacionCiudad(documentoIdentidad):
  pos_loc = 0
  print("Documento de  identificaión: ",documentoIdentidad)
  for i in range(0,len(pasajeros)):
    if pasajeros[i][1] == documentoIdentidad:
      pos_loc = i
      print("Encontrado")
      print("Pasajero con DNI:",pasajeros[pos_loc][1],"viaja a ",lista_pasajeros[pos_loc][2])
      break
    else:
      # print("Pasajero con ese DNI no encontrado.")
      pass
  
def conteoCiudad(ciudad):
  cnt_ciudad = 0
  print("Ciudad: ",ciudad)  
  for i in range(0,len(pasajeros)):
    if pasajeros[i][2] == ciudad:
      cnt_ciudad += 1
  print("El número de pasajeros que va a",ciudad,"es",cnt_ciudad) 

def verif_dni_pais(documentoIdentidad):
  l_departamentos = leer_archivos()
  print("El DNI seleccionado es:",documentoIdentidad)
  pos_loc = 0 
  for i in range(0,len(pasajeros)):
    if lista_pasajeros[i][1] == documentoIdentidad:
      pos_loc = i
      break
  ciudad = pasajeros[pos_loc][2]
  # print(ciudad)
  pos_loc2 = 0
  for i in range(0,len(l_departamentos)):
    if l_departamentos[i][1] == ciudad:
      pos_loc2 = i
      break
  # print(lista_departamentos[pos_loc2])
  print("El pasajero con DNI:",documentoIdentidad,"viaja al pais:",l_departamentos[pos_loc2][0])
  
def verif_pais_person(pais):
  cnt_ciudad = 0
  l_departamentos = leer_archivos()
  print("El país seleccionado es:",pais)
  pos_loc = 0 
  for i in range(0,len(l_departamentos)):
    if l_departamentos[i][0] == pais:
      pos_loc = i
      break
  ciudad = l_departamentos[pos_loc][1]
  for i in range(0,len(pasajeros)):
    if pasajeros[i][2] == ciudad:
      cnt_ciudad += 1
  print("Al pais de ",l_departamentos[pos_loc][0],"viajan",cnt_ciudad,"pasajeros")

def menu_iter():
  # Menu
  l=True # Declaración de la variable de control
  while l==True:
    os.system("clear")
    print("||Programa Pasajeros Viaje.\n")
    print("1. Agregar pasajeros a la lista de viajeros. \n2. Agregar ciudades a la lista de ciudades. \n3. Dado el DNI (cédula) de un pasajero, ver a que ciudad viaja. \n4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.\n5. Dado el DNI (cédula) de un pasajero, ver a que país viaja. \n6. Dado un país, mostrar cuántos pasajeros viajan a esa ciudad.  \n7. Salir del programa.")
    opc=int(input("Digite opción: "))
    if opc==1:
      print("Opcion 1 seleccionada")
      ingrearPasajero()
      print("Presione cualquier tecla para continuar.")
      input()
        
    elif opc==2:
      print("Opcion 2 seleccionada")
      print("Para esta opción se implementó la lectura de un csv que contiene todas las ciudades y países del mundo. \nConsideración: Según normas internacionales Escocia no es un país por lo que no aparecerá en la lista.")
      print("\nPresione cualquier tecla para continuar.")
      opc2=(input())
      menu_iter()
    elif opc==3:
        print("Opcion 3 seleccionada")
        documentoIdentidad = int(input("Digite el DNI a consultar: "))
        verificacionCiudad(documentoIdentidad)
        print("Presione cualquier tecla para continuar.")
        input()
        menu_iter()
  
    elif opc==4:
      print("Opcion 4 seleccionada")
      ciudad=str(input("Digite ciudad a consultar: "))
      conteoCiudad(ciudad)
      print("Presione cualquier tecla para continuar.")
      input()
      menu_iter()

    elif opc==5:
      print("Opcion 5 seleccionada")
      documentoIdentidad=int(input("Digite el DNI a consultar: "))
      verif_dni_pais(documentoIdentidad)
      print("Presione cualquier tecla para continuar.")
      input()
      menu_iter()

    elif opc==6:
      print("Opcion 6 seleccionada")
      pais=str(input("Digite pais a consultar: "))
      verif_pais_person(pais)
      print("Presione cualquier tecla para continuar.")
      input()
      menu_iter()
    
    elif opc==7:
        print("Programa terminará.")

        break
  return






