
from keras import backend as k
from PIL import Image
import mtcnn as mtcnn
import os
import tensorflow as tf
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.models import load_model

from keras import layers
from keras import models


#
# model = load_model('facenet_keras.h5')
#
# ##Details
# print(model.inputs)
# print(model.outputs)
# print(mtcnn.__version__)
#
# ## load image
# image = Image.open('me.JPG')
# image = image.convert('RGB')
# pixels = np.asarray(image)
# print(pixels)
#
# detector = MTCNN()
# results = detector.detect_faces(pixels)
#
#
# x1, y1, width, height = results[0]['box']
# x1, y1 = abs(x1), abs(y1)
# x2, y2 = x1 + width, y1 + height
#
# ## extract face
# face = pixels[y1:y2, x1:x2]
#
# # resize pixels to the model size
# image = Image.fromarray(face)
# image = image.resize((160, 160))
# face_array = asarray(image)

# function for face detection with mtcnn
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN

# extract a single face from a given photograph
def extract_face(filename, required_size=(160, 160)):
	# load image from file
	image = Image.open(filename)
	# convert to RGB, if needed
	image = image.convert('RGB')
	# convert to array
	pixels = asarray(image)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	results = detector.detect_faces(pixels)
	# extract the bounding box from the first face
	x1, y1, width, height = results[0]['box']
	# bug fix
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	# extract the face
	face = pixels[y1:y2, x1:x2]
	# resize pixels to the model size
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array

# load the photo and extract the face
pixels = extract_face('me.JPG')
img = Image.fromarray(pixels, 'RGB')
img.save('my_detected_face.png')
img.show()
