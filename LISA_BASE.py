import tensorflow as tf
import matplotlib.pyplot as plt

# Cargar el modelo pre-entrenado
model = tf.keras.applications.VGG16(weights='imagenet', include_top=True)

# Cargar y preprocesar la imagen de entrada
image_path = 'ruta/a/la/imagen.jpg'
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
input_image = tf.keras.preprocessing.image.img_to_array(image)
input_image = tf.keras.applications.vgg16.preprocess_input(input_image)
input_image = tf.expand_dims(input_image, axis=0)

# Generar la predicción de la imagen
predictions = model.predict(input_image)
decoded_predictions = tf.keras.applications.vgg16.decode_predictions(predictions, top=1)[0]
predicted_label = decoded_predictions[0][1]
confidence = decoded_predictions[0][2]

# Mostrar la imagen y la etiqueta predicha
plt.imshow(image)
plt.title(f'Predicted label: {predicted_label} (Confidence: {confidence:.2f})')
plt.axis('off')
plt.show()
