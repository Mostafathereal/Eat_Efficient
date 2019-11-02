
from keras import backend as k
# from keras.applications.inception_v3 import InceptionV3
# from keras.applications import InceptionResNetV2
# from keras.models import Model, model_from_json
# from keras.preprocessing.image import ImageDataGenerator
# from keras.layers import Dense, Flatten, Dropout, Conv2D
# from keras import optimizers

# example of loading the keras facenet model
from keras.models import load_model

from keras import layers
from keras import models

model = load_model('facenet_keras.h5')


print("Hello")
