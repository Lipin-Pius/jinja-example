import json
import pprint as pp
data = json.load(open('tes.json'));
#pp.pprint(data)
#for item in data:
#    pp.pprint(item)
# pp.pprint(data['input']['shape'])
# for item in data['nodes']:
#     pp.pprint(item)

node = data['nodes']




link = data['links']
source =[]
dest =[]
for item in link:
    source.append(item['source']['id'])
    dest.append(item['target']['id'])
#
# print('Items')
# pp.pprint(item)
#
# print('Source list')
# pp.pprint(source)
# print('Target list')
# pp.pprint(dest)

# pp.pprint(list(set(source).difference(dest)))
# pp.pprint(list(set(dest).difference(source)))

start = list(set(source).difference(dest))[0]
end  = list(set(dest).difference(source))[0]
network =[];


def node_lookup(origin):
    for item in link:
        if origin == item['source']['id']:
            network.append(item['source'])
            next = item['target']['id']
            if next == end:
                network.append(item['target'])
            link.remove(item)
            node_lookup(next)
    # pp.pprint(link)

node_lookup(start)
