import tensorflow as tf

node = amazon-s3.storage.amazon-s3(node)
node = tf.layers.conv2d(filters=32, kernel_size=(3,3), activation=tf.nn.relu, input_shape=,node)
node = tf.layers.conv2d(filters=64, kernel_size=(3,3), activation=tf.nn.relu, input_shape=,node)
node = tf.layers.maxpooling2d(pool_size=(2,2),node)
node = tf.layers.dropout(rate=0.25,node)
node = tf.layers.flatten(node)
node = tf.layers.dense(units=128, activation=tf.nn.relu,node)
node = tf.layers.dropout(rate=0.5,node)
node = tf.layers.dense(units=10, activation=tf.nn.softmax,node)
node = tf.train.AdamOptimizer.adam(node)
node = tf.losses.categorical_crossentropy(node)