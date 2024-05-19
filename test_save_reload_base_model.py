#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("_ Reloaded objects __")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
    
print("__ create a new object __")
