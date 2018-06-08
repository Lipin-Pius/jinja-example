import json
import pprint as pp
from jinja2 import FileSystemLoader, Environment
nodes={
    'data':[],
    'network':[],
    'optimzer':[]
}

# result_set={
#     'data_type':data['data_type'],
#     'input_shape': data['input_shape'][-1,1],
#     'data':'',
#     'network':'',
#     'loss_optimizer':'',
#     'learning_rate':''
# }

def node_lookup(origin):
    for item in link:
        if origin == item['source']['id']:
            network.append(item['source'])
            next_node = item['target']['id']
            if next_node == end:
                network.append(item['target'])
            link.remove(item)
            node_lookup(next_node)

# @node_lookup:
# The nodes are ordered

data = json.load(open('network.json', 'r'));

link = data['links']
source = []
dest = []
for item in link:
    source.append(item['source']['id'])
    dest.append(item['target']['id'])

start = list(set(source).difference(dest))[0]
end  = list(set(dest).difference(source))[0]
network =[];

# @28, 27: id of start and ending nodes are found

node_lookup(start)
# All nodes are sequentially ordered and stored in a list network
# the first element of network will be the first node to be processed




i = 0
for node in network:
    name = node['type'] + str(i)
    node['name']=name
    i = i+1

# give name to each node name is a valid identifier
for node in network:
    nodes[{
        'network':'network',
        'storage':'data',
        'loss': 'optimzer',
        'optimizer': 'optimzer'
    }[node['category']]].append(node)

# divided the network into input, network and optimzer

def lookup_category(x):
    return {
        'network':'tf.layers',
        'optimizer':'tf.train',
        'loss':'tf.losses',
        'storage':'aws.ec2'
    }[x]

def lookup_type(x):
    types={
        'maxpooling2d':'max_pooling2d',
        'adam':'AdamOptimizer'
    }
    if x in types:
        return types[x]
    else:
        return x

def parse_network_params(node, prev):
        keys = node['_def']['defaults'].keys()
        input = prev

        parameter_list = input + ','
        if 'activation' in keys:
            node['activation']='tensorflow.nn.'+node['activation']
        if any(keys):
            for item in keys:
                if node[item] is not "":
                    parameter_list = parameter_list + ' ' + item + ' = ' + node[item] + ','
        if node['type'] == 'maxpooling2d':
            parameter_list = parameter_list + ' strides=[1,1],'

        return parameter_list[:-1]



result = ''

for item in range(len(nodes['network'])):
        # pp.pprint(nodes['network'][item])
        # print(lookup_category(nodes['network'][item]['category']))
        if item == 0:
            result = result + nodes['network'][item]['name'] + ' = ' + lookup_category(nodes['network'][item]['category']) + '.' + lookup_type(nodes['network'][item]['type']) + '('+parse_network_params(nodes['network'][item],data['data_type'])+')\n'
        else:
            result = result + nodes['network'][item]['name'] + ' = ' + lookup_category(nodes['network'][item]['category']) + '.' + lookup_type(nodes['network'][item]['type']) + '('+parse_network_params(nodes['network'][item],nodes['network'][item-1]['name'])+')\n'
print(result)

result_set={
    'data_type':data['data_type'],
    'input_shape': data['input']['shape'],
    'data':'',
    'network':'',
    'loss_optimizer':'',
    'learning_rate':''
}

result_set['network'] = result


template = Environment(loader=FileSystemLoader('pytemplate')).get_template('template.py')
output = template.render({'data': result_set})

open('generated.py', 'w').write(output)
