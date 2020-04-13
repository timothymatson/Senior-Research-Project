from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import tensorflow as tf
from sklearn.model_selection import StratifiedKFold
import numpy as np
import json

# Code source: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

img_width, img_height = 150, 150

train_data_dir = './train'
#validation_data_dir = './validation'
#nb_train_samples = 168
#nb_validation_samples = 101
epochs = 10
batch_size = 256

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)


model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy',
                tf.keras.metrics.FalsePositives(name='fp'),
                tf.keras.metrics.FalseNegatives(name='fn'),
                tf.keras.metrics.TruePositives(name='tp'),
                tf.keras.metrics.TrueNegatives(name='tn'),
              ])

datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    validation_split=0.2)
    
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary',
    subset='training')
    
valid_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary',
    subset='validation')

model.fit_generator(
	train_generator,
	epochs=epochs,
	steps_per_epoch=538,
	validation_data=valid_generator,
	validation_steps=800)

model.save_weights('weights.h5')