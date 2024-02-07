import json
import os

def read_json(file):
  if not os.path.isfile(file):
    with open(file, 'w') as f:
      json.dump([], f)
    return []
  with open(file, 'r') as f:
    data = json.load(f)
    return data
  
def write_json(data, file='users.json'):
  with open(file, 'w') as f:
    json.dump(data, f)

