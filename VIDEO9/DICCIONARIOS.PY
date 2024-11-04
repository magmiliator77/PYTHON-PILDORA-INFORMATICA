midiccionario={"Alemania":"Berlin","Francía":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
midiccionario["Italia"]="Lisboa"
print(midiccionario)

midiccionario["Italia"]="Roma"
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)


#Esto nos permite saber el valor asignado a esta clave Alemania --> Berlin


#------------------------------------------------------------------------------#
print("----------------------------")



midiccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)

#-------------------------------------------------------------------------------#
print("----------------------------")

mitupla=["España", "Francía", "Reino Unido", "Alemania"]
midiccionario3={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario3[mitupla[2]])

#-------------------------------------------------------------------------------#
print("----------------------------")

midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3["Anillos"])

#Aqui estamos creando una tupla dentro de un diccionario

#-------------------------------------------------------------------------------#
print("----------------------------")

midiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4["Anillos"])

#Aqui estamos creando un diccionario dentro de otro adeamas de la tupla

#-------------------------------------------------------------------------------#
print("----------------------------")

midiccionario5={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario5.keys()) #Nos da todas la claves del diccionario
print(midiccionario5.values()) #Nos da todos los elementos del diccionario
print(len(midiccionario5)) #Nos da la longitud del diccionario, refiriendose al numero de claves por el que está formado