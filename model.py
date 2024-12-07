import tensorflow as tf

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(3, 3)), #1 layer
        tf.keras.layers.Dense(128, activation='relu'),#2 layer
        tf.keras.layers.Dense(64, activation='relu'),#2 layer
        tf.keras.layers.Dense(32, activation='relu'),#2 layer
        tf.keras.layers.Dense(9, activation='softmax')  # Predict probabilities for each cell
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
