import psycopg2 as cv
import numpy as nm
conexion1 = cv.connect(database="tiendaElectronica", user="postgres", password="Gm+2001juangym")
cursor1=conexion1.cursor()
cursor1.execute("SELECT * from ejemplo01.musicos")
for fila in cursor1:
 print(fila)
cursor1.execute("insert into ejemplo01.musicos (codmusico,nombre,apellido,ciudad_origen) values('57','ryan','castro','medallo')")
#cursor1.execute("delete from ejemplo01.musicos where nombre='maluma'")
conexion1.commit()
cursor1.execute("SELECT * from ejemplo01.musicos")
print(' \n\nse insertaron los datos nuevos: \n\n')
usuarios=cursor1.fetchall()
for u in usuarios:
  print(u)
conexion1.close()
