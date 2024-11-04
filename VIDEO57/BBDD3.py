import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")






#productos=miCursor.fetchall()

#print(productos)









"""

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    
    ("pelota", 20, "jugueteria"),
    ("pantalon", 15, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 45, "ceramica"),
    ("pantalones", 35, "confeccion")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")

"""
miConexion.commit()

miConexion.close()