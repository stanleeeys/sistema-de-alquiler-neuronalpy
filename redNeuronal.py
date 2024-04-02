import tensorflow as tf
import matplotlib.pyplot as plt

"""
ciudad (0), m^2, nº hab, nº planta, ascensor (0-1), exterior (0-1), 
estado (0 no rehabilitado, 1 rehab, 2 nuevo), céntrico (0, 1)
"""

features = [(0, 54, 2, 4, 0, 1, 0, 0),
            (0, 152, 2, 4, 1, 1, 3, 1),
            (0, 64, 3, 4, 0, 1, 0, 0),
            (0, 154, 5, 4, 1, 1, 1, 1),
            (0, 100, 1, 5, 1, 1, 1, 0),
            (0, 140, 5, 2, 1, 1, 2, 0),
            (0, 120, 3, 2, 1, 1, 1, 1),
            (0, 70, 2, 3, 1, 1, 1, 0),
            (0, 60, 2, 2, 0, 1, 1, 1),
            (0, 129, 3, 18, 1, 1, 2, 1),
            (0, 93, 1, 3, 1, 1, 2, 0),
            (0, 52, 2, 2, 0, 1, 1, 1),
            (0, 110, 3, 5, 1, 1, 1, 1),
            (0, 63, 3, 2, 1, 1, 1, 0),
            (0, 160, 1, 4, 1, 1, 2, 0)
            ]
targets = [750, 2000, 650, 1500, 900, 1000, 1300, 750, 900, 1800, 975, 880, 1400, 750, 1050]

capaEntrada = tf.keras.layers.Dense(units=8, input_shape=[8])
capaOculta = tf.keras.layers.Dense(units=8)
capaSalida = tf.keras.layers.Dense(units=1)

modelo = tf.keras.Sequential([capaEntrada, capaOculta, capaSalida])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

print('Inicio de entrenamiento...')
historial = modelo.fit(features, targets, epochs=1000, verbose=False)
print('Modelo entrenado!')

plt.xlabel('#Época')
plt.ylabel('Mágnitud de pérdida')
plt.plot(historial.history['loss'])
plt.show()

modelo.save('pisos_alquiler.h5')

