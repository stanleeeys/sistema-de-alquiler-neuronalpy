import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

"""
ciudad (0), m^2, nº hab, nº planta, ascensor (0-1), exterior (0-1), 
estado (0 no rehabilitado, 1 rehab, 2 nuevo)
"""

features = np.array([
    [0, 54, 2, 4, 0, 1, 0, 13.6929403, -89.2181911],
    [0, 152, 2, 4, 1, 1, 3, 13.6929403, -89.2181911],
    [0, 64, 3, 4, 0, 1, 0, 13.6929403, -89.2181911],
    [0, 154, 5, 4, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 100, 1, 5, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 140, 5, 2, 1, 1, 2, 13.6929403, -89.2181911],
    [0, 120, 3, 2, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 70, 2, 3, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 60, 2, 2, 0, 1, 1, 13.6929403, -89.2181911],
    [0, 129, 3, 18, 1, 1, 2, 13.6929403, -89.2181911],
    [0, 93, 1, 3, 1, 1, 2, 13.6929403, -89.2181911],
    [0, 52, 2, 2, 0, 1, 1, 13.6929403, -89.2181911],
    [0, 110, 3, 5, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 63, 3, 2, 1, 1, 1, 13.6929403, -89.2181911],
    [0, 160, 1, 4, 1, 1, 2, 13.6929403, -89.2181911]
])
targets = np.array([750, 2000, 650, 1500, 900, 1000, 1300, 750, 900, 1800, 975, 880, 1400, 750, 1050])

# Definir capas del modelo
capaEntrada = tf.keras.layers.Dense(units=9, input_shape=[9])
capaOculta = tf.keras.layers.Dense(units=9)
capaSalida = tf.keras.layers.Dense(units=1)

# Construir modelo
modelo = tf.keras.Sequential([capaEntrada, capaOculta, capaSalida])

# Compilar modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Entrenar modelo
print('Inicio de entrenamiento...')
historial = modelo.fit(features, targets, epochs=1000, verbose=False)
print('Modelo entrenado!')

# Visualizar pérdida durante el entrenamiento
plt.xlabel('#Época')
plt.ylabel('Magnitud de pérdida')
plt.plot(historial.history['loss'])
plt.show()

# Guardar modelo
modelo.save('pisos_alquiler.h5')