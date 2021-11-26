import os
import json
from indice import Indice
from revista import Revista
from registro import Registro
print("Bienvenido!")

class main:
	tablaPrincipal = []
	tablaSeriales = Indice([], False)
	tablaPalabras = Indice([], False)
	indicesDeRevistasEliminadas = []
	quitPrograma = False
	yaCargo = False

def switch(selection):
	if(selection==1):
		registrar()
	elif(selection==2):
		consultarPorSerial()
	elif(selection==3):
		comprarPorSerial()
	elif(selection==4):
		reabastecerPorSerial()
	elif(selection==5):
		consultarPorPalabra()
	elif(selection==6):
		eliminar()
	elif(selection==7):
		compactar()
	elif(selection==0):
		saveAndQuit()
	return

def saveAndQuit():
	main.quitPrograma = True
	guardar()
	return
	
	

def registrar():
	serial = requestSerial()
	titulo = requestTitulo()
	precio = int(requestPrecio())
	stock = int(requestStock())
	nuevaRevista = Revista(serial, titulo, precio, stock)
	rrc = agregarRevista(nuevaRevista)
	nuevoSerial = Registro(rrc, serial)
	main.tablaSeriales.get_tabla().append(nuevoSerial)
	main.tablaSeriales.sort()

	palabra = ""
	nuevaPalabra = ""
	for letra in titulo:
		
		if(letra == " " and palabra != ""):
			nuevaPalabra = Registro(rrc, palabra)
				
			main.tablaPalabras.get_tabla().append(nuevaPalabra)
			palabra = ""	
		if letra != " ":
			palabra += letra	
	
	else:
		nuevaPalabra = Registro(rrc, palabra)
		
		if palabra != "" and palabra != " ":		
			main.tablaPalabras.get_tabla().append(nuevaPalabra)
		
		palabra = ""

		
	main.tablaPalabras.sort()

	print("revista registrada con exito!!")

	
	return

def requestSerial():
	serial = input("Ingrese el serial de la revista: ")
	serialYaExiste = True
	tieneLetras = False
	
	while(len(serial) != 8 or tieneLetras):
		
		serial = input("por favor introduzca un serial que sea de 8 digitos, que no tenga letras: ")
		tieneLetras = False

		for digit in serial:
			try:
				digit = int(digit)
			except ValueError:
				tieneLetras = True

	while(serialYaExiste):
		serialYaExiste = False
		rrc = None
		
		if len(main.tablaSeriales.get_tabla()) == 0:
			return serial
		
		rrc = main.tablaSeriales.busquedaBinaria(serial)
		if len(rrc) > 0:
			serialYaExiste = True
			print("serial que introdujo ya esta asignado a una revista, introduzca otro ")
			serial = requestSerial()
	
	return serial

def requestTitulo():
	titulo = input("Ingrese el titulo de la revista: ")
	
	estaVacio = True
	esMuyCorto = True
	esMuyLargo = True
	noTieneLetras = True

	while(esMuyCorto or esMuyLargo  or estaVacio or noTieneLetras):
		
		for letra in titulo:
			if letra != " ":
				noTieneLetras = False

		if len(titulo) != 0:
			estaVacio = False

		if len(titulo) > 1:
			esMuyCorto = False

		if len(titulo) < 40:
			esMuyLargo = False
			
		if not estaVacio and not esMuyCorto and not esMuyLargo and not noTieneLetras:
			break

		titulo = input("titulo es muy largo, o no contiene letras, o es muy corto, ingrese un titulo que no tenga mas de 40 caracteres: ")
		estaVacio = True
		esMuyCorto = True
		esMuyLargo = True
		noTieneLetras = True

	return titulo

def requestPrecio():
	precio = input("Precio unitario de la revista a registrar: ")

	if(precio == ""):
		print("intente de nuevo")
		precio = requestPrecio()

	tieneLetras = True
	while(tieneLetras):
		tieneLetras = False

		for digit in precio:
			try:
				digit = int(digit)
			except ValueError:
				tieneLetras = True
				print("intente de nuevo")
				precio = requestPrecio()
	
	while(len(precio) > 3):
		print("no se admite precios mayores de 3 digitos, ingrese un precio nuevo.")
		precio = requestPrecio()
	
	return precio

def requestStock():
	stock = input("Stock de esta revista?: ")
	if stock == "0" or stock == "00":
		print("intente de nuevo")
		stock = requestStock()

	while(len(stock) > 2):
		stock = input("no se admite stocks mayores de 2 digitos, ingrese un stock correcto: ")
	
	tieneLetras = True
	while(tieneLetras):
		tieneLetras = False

		for digit in stock:
			try:
				digit = int(digit)
			except ValueError:
				tieneLetras = True
				print("probablemente introdujo una letra, intente de nuevo")
				stock = requestStock()
		
	return stock

def agregarRevista(nuevaRevista):
        rrc = len(main.tablaPrincipal)
        main.tablaPrincipal.append(nuevaRevista)
        return rrc

def consultarPorSerial():
	revistaNoEncontrada = True
	serial = ""
	rrc = None
	revista = None
	while revistaNoEncontrada:
		serial = input("ingrese el serial: ")

		while(len(serial) != 8):
			serial = input("serial no es valido intente de nuevo: ")

		rrc = main.tablaSeriales.busquedaBinaria(serial)

		if len(rrc) == 0 or not main.tablaPrincipal[rrc[0]].get_enStock():
			print("no hay coincidencias :( intente de nuevo con otro serial...")
		
		else:
			revistaNoEncontrada = False

	revista = main.tablaPrincipal[rrc[0]]

	print("Resultado de la busqueda:")
	print("Titulo: " + revista.get_titulo())
	print("Precio: " + str(revista.get_precio()) + "$")
	print("Ejemplares disponibles: " + str(revista.get_stock()))

	return rrc

def comprarPorSerial():
	rrc = consultarPorSerial()
	tieneLetras = True
	revista = main.tablaPrincipal[rrc[0]]
	if not revista.get_enStock() or revista.get_stock() == 0:
		print("lo sentimos, no hay ejemplares de esta revista disponible :(")
		return
	cantidad = input("ingrese la cantidad de revistas que quiere comprar: ")
	
	insuficienteStock = True
	while(insuficienteStock):
		
		tieneLetras = True
		while(len(cantidad) < 1 or len(cantidad) > 2 or tieneLetras ):
			
			
			tieneLetras = False

			for digit in cantidad:
				try:
					digit = int(digit)
				except ValueError:
					tieneLetras = True
			if(tieneLetras):
				cantidad = input("por favor introduzca una cantidad valida de maximo 2 digitos: ")
					
			

		if(int(cantidad) <= revista.get_stock()):
			insuficienteStock = False
		else:
			print("no hay suficientes revistas disponibles, intente con un numero mas bajo :(")
			cantidad = input("ingrese la cantidad de revistas que quiere comprar: ")

	precio = revista.get_precio()
	stock = revista.get_stock() - int(cantidad)
	print("Precio total: " + str(precio * int(cantidad)) + "$")
	
	main.tablaPrincipal[rrc[0]].set_stock(stock)
	print("Gracias por su compra!!")

	return

def reabastecerPorSerial():
	rrc = consultarPorSerial()
	tieneLetras = True
	revista = main.tablaPrincipal[rrc[0]]
	if not revista.get_enStock():
		print("lo sentimos, Esta revista no existe :(")
		return
	cantidad = input("ingrese la cantidad de ejemplares de esta revista que quiere añadir: ")
	masDeCienRevistas = True
	while(masDeCienRevistas):
		
		tieneLetras = True

		while(len(cantidad) < 1 or len(cantidad) > 2 or tieneLetras ):
			
			
			tieneLetras = False

			for digit in cantidad:
				try:
					digit = int(digit)
				except ValueError:
					tieneLetras = True
			
			if(tieneLetras) or len(cantidad) > 2:
				cantidad = input("por favor introduzca una cantidad valida de maximo 2 digitos: ")
					
			

		if(int(cantidad) + revista.get_stock() <= 99):
			masDeCienRevistas=False
		else:
			masDeCienRevistas=True
			print("lo sentimos, no pueden haber mas de 99 ejemplares en el inventario, intente con un numero mas bajo.")
			cantidad = input("ingrese la cantidad de ejemplares de esta revista que quiere añadir:")

	stock = revista.get_stock() + int(cantidad)
	main.tablaPrincipal[rrc[0]].set_stock(stock)
	print("los ejemplares han sido reabastecidos satisfactoriamente :)")

	return

def cargar():
	try:
		json_file = open('datos.txt', 'r', encoding='utf-8')
		try:
			datos = json.load(json_file)
			lista = list(datos.values())
			
			for listaAux in lista:
				revista = Revista(listaAux[0], listaAux[1], listaAux[2], listaAux[3], listaAux[4])
				main.tablaPrincipal.append(revista)
		except json.JSONDecodeError:
			return

		json_file.close()
		index = 0
		for revista in main.tablaPrincipal:
			rrc = index
			nuevoSerial = Registro(rrc, revista.get_serial())
			main.tablaSeriales.get_tabla().append(nuevoSerial)
			

			palabra = ""
			nuevaPalabra = ""
			for letra in revista.get_titulo():
				
				if(letra == " " and palabra != ""):
					nuevaPalabra = Registro(rrc, palabra)
						
					main.tablaPalabras.get_tabla().append(nuevaPalabra)
					palabra = ""	
				if letra != " ":
					palabra += letra	
			
			else:
				nuevaPalabra = Registro(rrc, palabra)
				
				if palabra != "" and palabra != " ":		
					main.tablaPalabras.get_tabla().append(nuevaPalabra)
				
				palabra = ""
			
			index += 1
			
		main.tablaSeriales.sort()
		main.tablaPalabras.sort()

	except FileNotFoundError:
		return

def guardar():

	for rrcaux in main.indicesDeRevistasEliminadas:
		main.tablaPrincipal.pop(rrcaux)

	try:
		os.remove('datos.txt')
	except FileNotFoundError:
		pass

	json_file = open('datos.txt', 'w', encoding='utf-8')
	dict = {}
	indice = 0
	listaAux = []
	for revista in main.tablaPrincipal:
		listaAux.append(revista.get_serial())
		listaAux.append(revista.get_titulo())
		listaAux.append(revista.get_precio())
		listaAux.append(revista.get_stock())
		listaAux.append(revista.get_enStock())

		dict[indice] = listaAux
		listaAux=[]
		indice+=1

	json.dump(dict, json_file)
	json_file.close()

def consultarPorPalabra():
	palabras = input("ingrese 1 o 2 palabras para buscar (ejemplo: batman superman ): ")
	palabra = ""
	rrcList =[]
	listaDePalabras = []
	for letra in palabras:
		
		if(letra == " " and palabra != ""):
			listaDePalabras.append(palabra)
			
			palabra = ""	
		if letra != " ":
			palabra += letra	
	
	else:
		
		if palabra != "" and palabra != " ":		
			listaDePalabras.append(palabra)
		palabra = ""

	rrcDePalabra1 = main.tablaPalabras.busquedaBinaria(listaDePalabras[0])
	if(len(listaDePalabras) > 1):
		rrcDePalabra2 = main.tablaPalabras.busquedaBinaria(listaDePalabras[1])
		rrcList = intersect(rrcDePalabra1, rrcDePalabra2)
	else:
		rrcList = rrcDePalabra1

	if len(rrcList) == 0:
		print("no se encontraron coincidencias :(")
		return
	else:
		print("se encontraron las siguientes revistas relacionadas con su busqueda: ")
		for index in rrcList:
			if main.tablaPrincipal[index].get_enStock():
				revista = main.tablaPrincipal[index]
				print("--------------------------------------")
				print("Titulo: " + revista.get_titulo())
				print("Precio: " + str(revista.get_precio()))
				print("Ejemplares disponibles: " + str(revista.get_stock()))
				print("--------------------------------------")
			elif(len(rrcList) == 1):
				print("no se encontraron coincidencias :(")
	return
	
def intersect(rrcDePalabra1, rrcDePalabra2):
	rrcList = []
	
	for element in rrcDePalabra1:
		for element2 in rrcDePalabra2:
			if element == element2:
				rrcList.append(element)

	return rrcList

def requestSerialToEliminate():
	serial = input("Ingrese el serial de la revista que quiere eliminar: ")
	tieneLetras = False
	rrc = None
	while(len(serial) != 8 or tieneLetras):
		
		serial = input("por favor introduzca un serial que sea de 8 digitos, que no tenga letras: ")
		tieneLetras = False

		for digit in serial:
			try:
				digit = int(digit)
			except ValueError:
				tieneLetras = True

	
	if len(main.tablaSeriales.get_tabla()) == 0:
		print("no hay revistas registradas")
		return None
	

	rrc = main.tablaSeriales.busquedaBinaria(serial)
	if len(rrc) > 0:
		
		return rrc
	else:
		print("no existe una revista con ese serial")
		return None


def eliminar():
	rrcList = requestSerialToEliminate()
	if rrcList is None or len(rrcList) == 0:
		return 
	rrc = rrcList[0]
	main.tablaPrincipal[rrc].set_enStock(False)
	main.tablaSeriales.get_tabla()[rrc].set_enStock(False)
	main.indicesDeRevistasEliminadas.append(rrc)
	print("eliminacion exitosa")

	return

def compactar():
	try:
		for rrc in main.indicesDeRevistasEliminadas:
			main.tablaPrincipal.pop(rrc)

	except IndexError:
		print("no hay nada que compactar")

	index = 0
	main.tablaSeriales.set_tabla([]) 
	main.tablaPalabras.set_tabla([])
	for revista in main.tablaPrincipal:
		rrc = index
		nuevoSerial = Registro(rrc, revista.get_serial())
		main.tablaSeriales.get_tabla().append(nuevoSerial)
		

		palabra = ""
		nuevaPalabra = ""
		for letra in revista.get_titulo():
			
			if(letra == " " and palabra != ""):
				nuevaPalabra = Registro(rrc, palabra)
					
				main.tablaPalabras.get_tabla().append(nuevaPalabra)
				palabra = ""	
			if letra != " ":
				palabra += letra	
		
		else:
			nuevaPalabra = Registro(rrc, palabra)
			
			if palabra != "" and palabra != " ":		
				main.tablaPalabras.get_tabla().append(nuevaPalabra)
			
			palabra = ""
		
		index += 1
		
	main.tablaSeriales.sort()
	main.tablaPalabras.sort()
	print("se ha compactado el inventario :)")
	return
	
while not main.quitPrograma:

	if not main.yaCargo:
		cargar()
		main.yaCargo = True

	print("1 ----> registrar")
	print("2 ----> consultar por Serial")
	print("3 ----> comprar por serial")
	print("4 ----> Reabastecer por serial")
	print("5 ----> consultar por palabra")
	print("6 ----> eliminar")
	print("7 ----> compactar")
	print("0 ----> cerrar programa")
	selection = ''
	try:
		while(selection==''):
			selection = input("Ingrese el numero para lo que desee hacer: ")
		
		switch(int(selection))

	except ValueError:
		pass	
	
print("Hasta luego!!")

