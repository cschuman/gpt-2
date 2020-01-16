#!/usr/bin/env python3

import json

# some JSON:
x =  '''[{ "id":1,  "input":"It was a dark and stormy night", "attribution":"New York"},
        { "id":2,  "input":"It was a dark and stormy night", "attribution":"New York"},
        { "id":3,  "input":"It was a dark and stormy night", "attribution":"New York"},
        { "id":4,  "input":"It was a dark and stormy night", "attribution":"New York"}
        ]'''

# parse x:
y = json.loads(x)

for item in y:
  print(f'## {item["id"]}. {item["input"]}', end='\n\n')

  for i in range(3):
    print(f'### ITEM {item["id"]}.{i}', end='\n\n')
    print(f'> {item["attribution"]}', end='\n\n')
    print(f'***{item["input"]}***', end='\n\n')
  
  print('\n\n')

# the result is a Python dictionary:
# print(y["input"])