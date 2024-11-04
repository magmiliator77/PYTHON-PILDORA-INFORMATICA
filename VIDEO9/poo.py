				    #}-------------------------------------------+
class Coche():                                                  #|
	largoChasis=250												#|
	anchoChasis=120												#|---Propiedades del coche
	ruedas=4													#|
	enMarcha=False												#|
					#}-------------------------------------------+

#Metodo de la clase el self se refiere a que es de la clase, a que pertenece a la clase
	def arrancar(self):#<----------------------------------------------------------------+
		self.enMarcha=True														#		 |
																				#		 |
																				#		 |
																				#2 COMPORTAMIENTOS
																				#		 |
																				#        |
																				#        |
	def estado(self):#<------------------------------------------------------------------+
		if(self.enMarcha):
			return "El coche está en marcha"

		else:
			return "El coche está parado"


miCoche=Coche() #Instaciamos la clase (crear un objeto)




print("El largo del coche es: ",miCoche.largoChasis) 
print("El coche tiene:",miCoche.ruedas,"ruedas")

#Aqui lo que estamos haciendo es arrancar el coche, ya que estamos llamando al metodo
#arrancar, y estamos cambiando el valor enMarcha a true, poniendo siembre self ya que
#Este es del metodo
miCoche.arrancar() 

print(miCoche.estado())
