# Python templating using jinja2

test.py takes network.json as input and creates a list nodes saved in list.json.</br>

model.py takes list.json and template <i>python.py</i> and generates <i>generated.py</i>

output:

<p>amazon-s3storage0 = amazon.ec2.fetch_data()</p>

<p>conv2dnetwork1 = tensorflow.layers.conv2d(amazon-s3storage0, filters = 32, kernel_size = (3,3), activation = tensorflow.nn.relu)</p>
<p>conv2dnetwork2 = tensorflow.layers.conv2d(conv2dnetwork1, filters = 64, kernel_size = (3,3), activation = tensorflow.nn.relu)</p>
<p>maxpooling2dnetwork3 = tensorflow.layers.max_pooling2d(conv2dnetwork2, pool_size = (2,2))</p>
<p>dropoutnetwork4 = tensorflow.layers.dropout(maxpooling2dnetwork3, rate = 0.25)</p>
<p>flattennetwork5 = tensorflow.layers.flatten(dropoutnetwork4)</p>
<p>densenetwork6 = tensorflow.layers.dense(flattennetwork5, units = 128, activation = tensorflow.nn.relu)</p>
<p>dropoutnetwork7 = tensorflow.layers.dropout(densenetwork6, rate = 0.5)</p>
<p>densenetwork8 = tensorflow.layers.dense(dropoutnetwork7, units = 10, activation = tensorflow.nn.softmax)</p>
<p>adamoptimizer9 = tensorflow.train.AdamOptimizer(densenetwork8)</p>
<p>categorical_crossentropyloss10 = tensorflow.losses.categorical_crossentropy(adamoptimizer9)</p>
