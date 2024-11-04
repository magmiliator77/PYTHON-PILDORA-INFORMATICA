#Ejercicio 9: Mostrar la Fecha de un Evento Almacenada en una Tupla 

fecha_evento = (2023, 9, 14)

print(type(fecha_evento))

#MANERA 1
print('El evento programado será para la fecha:', fecha_evento)


#MANERA 2 -->  %i/%i/%i ESTO LO QUE HACE ES MAPEAR LOS ELEMENTO QUE HAY EN LA TUPLA
print('El evento programado será para la fecha: %i/%i/%i' % fecha_evento)

#MANERA 3 --> ESTO LO QUE NOS PERMITE ES DESENPAQUETAR LA TUPLA

año, mes, día = fecha_evento

print('El evento programado será para la fecha: {}/{}/{}'.format(año, mes, día))


print('El evento programado será para la fecha: {}/{}/{}'.format(día, mes, año))

















