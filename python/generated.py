w#!/bin/python
import tensorflow as tf

# Data
# Whatever amazon strategy

image = tf.reshape(x, [-1,28, 28,1])
# Network
conv2d1 = tf.layers.conv2d(image, filters = 32, kernel_size = (3,3), activation = tensorflow.nn.relu)
conv2d2 = tf.layers.conv2d(conv2d1, filters = 64, kernel_size = (3,3), activation = tensorflow.nn.relu)
maxpooling2d3 = tf.layers.max_pooling2d(conv2d2, pool_size = (2,2), strides=[1,1])
dropout4 = tf.layers.dropout(maxpooling2d3, rate = 0.25)
flatten5 = tf.layers.flatten(dropout4)
dense6 = tf.layers.dense(flatten5, units = 128, activation = tensorflow.nn.relu)
dropout7 = tf.layers.dropout(dense6, rate = 0.5)
dense8 = tf.layers.dense(dropout7, units = 10, activation = tensorflow.nn.softmax)

# loss & Optimization
learning_rate =
