import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

celsius=np.array([-40,-10,0,8,15,22,38] ,dtype=float)
fahrenheit=np.array([-40,14,32,46,59,77,100] ,dtype=float)

#capa=tf.keras.layers.Dense(units=1, input_shape=[1])   --una neurona de entrada y una de salida  
#modelo=tf.keras.Sequential([capa])

oculta1=tf.keras.layers.Dense(units=3, input_shape=[1])    
oculta2=tf.keras.layers.Dense(units=3)
salida=tf.keras.layers.Dense(units=1) 
modelo=tf.keras.Sequential([oculta1,oculta2,salida])  

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss='mean_squared_error'
)

print('comenzamos el entrenamiento')

historial=modelo.fit(celsius,fahrenheit,epochs=500,verbose=False)

print('modelo entrenado')
plt.title("errores por vueltas")
plt.xlabel("epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historial.history["loss"],marker=',',color='g')
plt.show()

print("hacer una prediccion")
resultado=modelo.predict([100.0])
resultado1=modelo.predict([38.0])
print("el resultado es"+ str(resultado)+"fahrenheit")
print("el resultado es"+ str(resultado1)+"fahrenheit")

print("variables internas del modelo")
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())