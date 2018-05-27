from django.shortcuts import render
import json
from jinja2 import Template
# Create your views here.
data = json.load(open('jinja.json'))
def index(request):
		return render(request, 'jinja/index.html', {'data': data} )
