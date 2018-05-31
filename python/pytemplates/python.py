import tensorflow as tf

{% for item in data.keys() %}
{{ data[item] }}
{% endfor %}