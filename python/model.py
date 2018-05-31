#This is just a test
#!/bin/python
from jinja2 import FileSystemLoader, Environment

import json
import pprint as pp


# Dictionary Used

nodes = {}

# Function Used

def lookup_category(x):
    return {
        'network':'tensorflow.layers',
        'optimizer':'tensorflow.train',
        'loss':'tensorflow.losses',
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

def parse_params(node, src):
    keys = node['_def']['defaults'].keys()
    input = nodes[src]['name']
    parameter_list = input + ','
    if 'activation' in keys:
        node['activation']='tensorflow.nn.'+node['activation']
    if any(keys):
        for item in keys:
            if node[item] is not "":
                parameter_list = parameter_list + ' ' + item + ' = ' + node[item] + ','

    return parameter_list[:-1]



def link_to_nodes(link):

    source_node = nodes[link['source']['id']]
    target_node = nodes[link['target']['id']]
    result = target_node['name'] + ' = ' + lookup_category(link['target']['category']) + '.' + lookup_type(link['target']['type']) + '(' + parse_params(link['target'],link['source']['id']) + ')'
    nodes[link['target']['id']]['op'] = result
    nodes[link['target']['id']]['complete'] = True
    nodes[link['source']['id']]['target'] = link['target']['id']


# pp.pprint(nodes)

def parse(start):
    try:
        return nodes[start]['op'] + '\n' + parse(nodes[start]['target'])
    except Exception as e:
        return ''



if __name__=='__main__':
    # pp.pprint(data)
    with open('network.json','r') as fp:
        data = json.load(fp)



    i = 0
    for node in data['nodes']:
        name = node['type'] + node['category'] + str(i)
        nodes[node['id']]={'name':name,
        'complete':False,
        'op':'',
        'target':''
        }
        i = i+1

    # pp.pprint(nodes)
    for item in data['links']:
        link_to_nodes(item)



    for item in data['links']:
        if not(nodes[item['source']['id']]['complete']):
            op = nodes[item['source']['id']]['name'] + ' = amazon.ec2.fetch_data()'
            op = op + '\n' + parse(item['source']['id'])
            break




    # templateEnvironment = Environment(loader='file')
    # template = templateEnvironment.get_template('python.py')
    # output = template.render({'data': op})

    with open('generated.py', 'w') as fp:
      fp.write(op)
    print(op)

# pp.pprint(result)
