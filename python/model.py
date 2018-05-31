#This is just a test
#!/bin/python
import pprint as pp
import json
from jinja2 import FileSystemLoader, Environment

def translate(x):
      data =  {
        'storage':'amazon-s3.storage', # I didn't know what to put here
        'network':'tf.layers',
        'relu':'tf.nn.relu',
        'softmax':'tf.nn.softmax',
        'optimizer':'tf.train.AdamOptimizer',
        'loss':'tf.losses'
      }
      if x in data:
            return data[x]
      else:
            return 0

def dict_parse(dict1):
      result = 'node = '
      result = result + translate(dict1['category'])
      result = result + '.' + dict1['type'] + '('
      if dict1['_def']:
            keys = dict1.keys()
            default = ['id', 'type', 'category', '_def']
            # print '**********************************************'
            for item in keys:
                  value = dict1[item]
                  if not value:
                        value = '\'\''
                  if item not in default and value:
                        if result[-1] == ',':
                              result = result + ' ' + item + '='
                        else:
                              if item not in default:
                                    result = result + item  + '='
                        x = translate(dict1[item])
                        if x:
                              result = result + x + ','
                        else:
                              result = result + dict1[item] + ','
            if result[-1] == ',':
                  result = result + 'node)'
            elif result[-1] == '(':
                  result = result + 'node)'
            else:
                  result = result + ', node)'
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
