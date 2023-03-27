import inspect

def create_dictionary(key):
   d = dict();
   d[key] = str(inspect.signature(create_dictionary))
   return d



print (create_dictionary(12475))