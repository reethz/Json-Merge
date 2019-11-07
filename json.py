# Python program showing that 
# json support different primitive 
# types 

import json 

# list conversion to Array 
print(json.dumps(['Welcome', "to", "Json"])) 

# tuple conversion to Array 
print(json.dumps(("Welcome", "to", "Hello World"))) 

# string conversion to String 
print(json.dumps("Hi")) 

# int conversion to Number 
print(json.dumps(555)) 

# float conversion to Number 
print(json.dumps(23.572)) 

# Boolean conversion to their respective values 
print(json.dumps(True)) 
print(json.dumps(False)) 

# None value to null 
print(json.dumps(None)) 
