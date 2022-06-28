import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import math
import numpy as np

datos,metadatos= tfds.load('fashion_mnist',as_supervised=True,with_info=True)#para que se descarguen con todos los meta datos
print(metadatos)
datos_entrenamiento,datos_prueba=datos['train'],datos['test']#los separo los datos
name_classes=metadatos.features['label'].names 
print(name_classes)

#now i have normalizar of data passs od 0-255 to 0-1
 
def normalizar(imagenes,etiquetas):
    imagenes=tf.cast(imagenes, tf.float32)
    imagenes/=255 #pass of 255 to 1
    return imagenes,etiquetas
#nomalizer of data train and test

datos_entrenamiento=datos_entrenamiento.map(normalizar)
datos_prueba=datos_prueba.map(normalizar)

#usar memoria en lugar de disco aggg to cache



print("mostrando la primera imagen")

'''
for imagenes,etiquetas in datos_entrenamiento.take(1):
    break
imagenes=imagenes.numpy().reshape((28,28))#redireccionaer

plt.figure()
plt.imshow(imagenes,cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.xlabel(name_classes[etiquetas])
plt.show()

plt.figure(figsize=(10,10))
for i,(imagenes,etiquetas) in enumerate(datos_entrenamiento.take(25)):
    imagenes=imagenes.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagenes, cmap=plt.cm.binary)
    plt.xlabel(name_classes[etiquetas])
    plt.show()
'''
#comenzamos el modelo
print('comenzando el diseño del modelo')
model =  tf.keras.Sequential([

    tf.keras.layers.Flatten(input_shape=(28,28,1)),#1 because is black and white flatten=la aplasta a 1 sola dimension 
    tf.keras.layers.Dense(50,activation=tf.nn.relu),
    tf.keras.layers.Dense(50,activation=tf.nn.relu),#capaz ocultas con la funtion of activation relu 
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)#softmax se usa en la capa de salida en las redes de clasificacion
                                                      #hace que la suma de todos sea igual a 1 al final toma el de mayor numero
                                                 
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#to do the train is better separate for lotes

tamaño_lote=32
num_ejem_entrenamiento=metadatos.splits['train'].num_examples
num_ejem_pruebas=metadatos.splits['test'].num_examples
datos_entrenamiento=datos_entrenamiento.repeat().shuffle(num_ejem_entrenamiento).batch(tamaño_lote)#que se haga de manera aleatorio 
datos_prueba=datos_prueba.batch(tamaño_lote)

#entreno los datos
 
print('entrenando')

historial = model.fit(datos_entrenamiento, epochs=5, steps_per_epoch=math.ceil(num_ejem_entrenamiento/tamaño_lote))

print("mostrar el grafico")
 
plt.xlabel("#epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historial.history["loss"])
plt.show()

#predicciones 

predictions = model.predict(datos_prueba)
print(predictions[0])
arram=np.argmax(predictions[0])
print(arram)

for imagenes_prueba, etiquetas_prueba in datos_prueba.take(1):
  imagenes_prueba = imagenes_prueba.numpy()
  etiquetas_prueba = etiquetas_prueba.numpy()
  predicciones = model.predict(imagenes_prueba)
  
def graficar_imagen(i, arr_predicciones, etiquetas_reales, imagenes):
  arr_predicciones, etiqueta_real, img = arr_predicciones[i], etiquetas_reales[i], imagenes[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img[...,0], cmap=plt.cm.binary)

  etiqueta_prediccion = np.argmax(arr_predicciones)
  if etiqueta_prediccion == etiqueta_real:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(name_classes[etiqueta_prediccion],
                                100*np.max(arr_predicciones),
                                name_classes[etiqueta_real]),
                                color=color)
  
def graficar_valor_arreglo(i, arr_predicciones, etiqueta_real):
  arr_predicciones, etiqueta_real = arr_predicciones[i], etiqueta_real[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  grafica = plt.bar(range(10), arr_predicciones, color="#777777")
  plt.ylim([0, 1]) 
  etiqueta_prediccion = np.argmax(arr_predicciones)
  
  grafica[etiqueta_prediccion].set_color('red')
  grafica[etiqueta_real].set_color('blue')
  
filas = 5
columnas = 3
num_imagenes = filas*columnas
plt.figure(figsize=(2*2*columnas, 2*filas))
for i in range(num_imagenes):
  plt.subplot(filas, 2*columnas, 2*i+1)
  graficar_imagen(i, predicciones, etiquetas_prueba, imagenes_prueba)
  plt.subplot(filas, 2*columnas, 2*i+2)
  graficar_valor_arreglo(i, predicciones, etiquetas_prueba)
  plt.show()
  
