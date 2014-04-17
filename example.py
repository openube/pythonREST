#!/usr/bin/env python
""" Example run of the pythonREST server

To test, run this script (either python example.py or
as an executable ./python), and in a seperate terminal
call, for example (square root of 10): 

curl -X PUSH http://0.0.0.0:9090 -d '{"fun": "root_fun", "params" : {"n" : 10}}'
"""

import pythonrest

def square_fun(params):
    return str(params["n"]**2)

def root_fun(params):
    import math
    return str(math.sqrt(params["n"]))

pyserver = pythonrest.PyServer()
pyserver.add_post_fun(square_fun)
pyserver.add_post_fun(root_fun)

pyserver.run()