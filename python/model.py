import pprint as pp
import json
from jinja2 import FileSystemLoader, Environment

def translate(x):
      return {
        'storage':'amazon-s3.storage',
        'network':'tf.layers',
        'relu':'tf.nn.relu',
        'softmax':'tf.nn.softmax',
        'optimizer':'tf.train.AdamOptimizer',
        'loss':'tf.losses'
      }[x]

def dict_parse(dict1):
      result=''
      result = result + translate(dict1['category'])
      if dict1['_def']:
            result = result + '.' + dict1['type']+'()'
      return result;

fileLoader = FileSystemLoader('pytemplates')
templateEnvironment = Environment(loader = fileLoader)



# def dict_lookup(dict1, x):
#   return dict1[x];

result = {}

with open('list.json', 'r') as fp:
  data=json.load(fp)

# # pp.pprint(data)

# # print(dict_lookup(data[1]['_def'], 'defaults'))
j = 'a'
for i in range (0,len(data)):
      result[i]=dict_parse(data[i]);
     

template = templateEnvironment.get_template('python.py')
output = template.render({'data': result})
with open('generated.py', 'w') as fp:
  fp.write(output)
print(output)

# pp.pprint(result)