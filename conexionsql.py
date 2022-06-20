import psycopg2 as cv
import numpy as nm
from os import system
conexion1 = cv.connect(database="tiendaElectronica", user="postgres", password="Gm+2001juangym")
cursor1=conexion1.cursor()
cursor2=conexion1.cursor()
cursor1.execute("SELECT * from ejemplo01.musicos")
for fila in cursor1:
 print(fila)
cursor2.execute("insert into ejemplo01.musicos (codmusico,nombre,apellido,ciudad_origen) values('57','ñengo','flow','pr')")
#cursor2.execute("delete from ejemplo01.musicos where nombre='ñengo'")
conexion1.commit()
cursor2.execute("SELECT * from ejemplo01.musicos")
print(' \n\nse insertaron los datos nuevos: \n\n')

for fila in cursor2:
  print(fila)

conexion1.close()
