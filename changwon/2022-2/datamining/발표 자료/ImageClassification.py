from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open('test.jpg')
image.show()
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image.show()

#turn the image into a numpy array
image_array = np.asarray(image)
print(image_array)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)

######################
# TODO: labels.txt를 읽어서 이미지가 어떤 클래스를 가리키는지 출력하기
predicted_index = prediction[0].argmax()

f = open('labels.txt', 'r', encoding='utf-8')
lines = f.readlines()
for i, line in enumerate(lines):
    data = line.split(' ')
    index = int(data[0])
    label = data[1]

    if index == predicted_index:
        print(" ")
        print("======================")
        print("==========결과========")
        print(label)
        break

######################