import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")


variosProductos=[
 
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 10, "Ceramica"),
    ("Camion", 10, "Jugueteria")              
]

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall() #NOS DEVUELVE UNA LISTA CON TODOS LOS REGISTROS DE LA INTRUCCION SQL


for producto in variosProductos:

    print("Nombre articulo: ", producto[0], " Seccion: ", producto[2])


miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos) #Tantos interrognates como valores tengamos en la tabla



miConexion.commit()



miConexion.close()
