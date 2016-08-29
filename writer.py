import requests, json
from influxdb import InfluxDBClient

contents = requests.get('http://127.0.0.1:8181/onos/influxtest/api/test-node', auth=('user', 'password'))
data = [contents.json()]

print data

client = InfluxDBClient('127.0.0.1', 8086, 'user', 'password', 'example')
client.create_database('example')
client.write_points(data)
result = client.query('select value from ram_load_short;')
print("Result: {0}".format(result))
