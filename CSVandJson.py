#working with JSON
import json
JsonData = '{"name":"Laptop","isWorking":true,"os":"windows"}'
print(type(JsonData))
jsonasPython = json.loads(JsonData)
print(jsonasPython)
print(type(jsonasPython))