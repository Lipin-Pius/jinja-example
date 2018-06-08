#!/bin/python
import tensorflow as tf

# Data
# Whatever amazon strategy

{{data.data_type}} = tf.reshape(x, [-1,{{data.input_shape[1:-1]}},1])
# Network
{{data.network}}
# loss & Optimization
learning_rate = {{data.learning_rate}}
