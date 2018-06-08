import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets("var/MNIST/", one_hot=True)

# model

X_input = tf.placeholder(tf.float32, [None, 784]) # Still Questionable
y_input = tf.placeholder(tf.float32, [None, 10])  # Still Questionable

im_input = tf.reshape(X_input, [-1,28,28,1])  # Use formatted input shape as 28, 28

conv1 = tf.layers.conv2d(im_input, filters=32, kernel_size=(3,3), activation=tf.nn.relu)
conv2 = tf.layers.conv2d(conv1, filters = 64, kernel_size = (3,3), activation = relu)

pool1 = tf.layers.max_pooling2d(conv2, pool_size=(2,2), strides=[1,1]) # Add strides
dropout1 = tf.layers.dropout(pool1, rate=0.25)

flat1 = tf.layers.flatten(dropout1)
dense1 = tf.layers.dense(flat1, units = 128, activation = tf.nn.relu)

dropout2 = tf.layers.dropout(dense1, rate=0.5)
dense2 = tf.layers.dense(dropout2, units=10, activation= tf.nn.softmax)

# model ends here

#loss function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_input * tf.log(dense2), reduction_indices=[1]))
#optimiser -
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy) # learning rate
#calculating accuracy of our model
correct_prediction = tf.equal(tf.argmax(dense2,1), tf.argmax(y_input,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    epoch=15000
    batch_size=50
    for i in range(epoch):
        #batch wise training
        x_batch, y_batch = data.train.next_batch(batch_size)
        _,loss=sess.run([train_step, cross_entropy], feed_dict={X_input: x_batch,y_input: y_batch})
        #_, loss,acc=sess.run([train_step,cross_entropy,accuracy], feed_dict={x:input_image , y_: input_class})

        if i%500==0:
            Accuracy=sess.run(accuracy,
                               feed_dict={
                            X_input: data.test.images,
                            y_input: data.test.labels
                          })
            Accuracy=round(Accuracy*100,2)
            print("Loss : {} , Accuracy on test set : {} %" .format(loss, Accuracy))
        elif i%100==0:
            print("Loss : {}" .format(loss))
