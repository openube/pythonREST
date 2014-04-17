#!/usr/bin/env python
""" A simple RESTful client for parsing TCP requests in python

Defines two classes for creating a REST server for purpose of
executing arbitrary functions given parameters passed in JSON
format.
"""

import signal
import pyuv
import json

class Request(object):
    """ 
    A REST request passed to the server
    """
    def __init__(self, data):
        data = data.split("\n")
        self.method =  data[0]
        self.user_agent = data[1]
        self.host = data[2]
        self.content_type = data[5]
        self.data = json.loads(data[7])

    def get_fun_name(self):
        return self.data['fun']

    def get_params(self):
        if self.data['params'] is None:
            return None
        else:
            return self.data['params']


class PyServer(object):
    """
    REST server for calling functions in Python via TCP requests
    """
    def __init__(self, host="0.0.0.0", port=9090, post_funs=None):
        self.host = host
        self.port = port
        if post_funs is None:
            self.post_funs = {}
        else:
            self.post_funs = post_funs

    def add_post_fun(self, post_function):
        # post_function must be a function
        self.post_funs[post_function.__name__] = post_function

    def del_post_fun(self, post_function):
        # post_function can be a function or name of a function
        if hasattr(obj, '__call__'):
            x.pop(post_function.__name__)
        else:
            x.pop(post_function)

    def run(self):
        def on_read(client, data, error):
            if data is not None:
                request = Request(data)
                fun_name = request.get_fun_name()
                results = self.post_funs[fun_name](request.get_params())
                client.write(str(results))
                client.write("     \n")
            client.close()
            clients.remove(client)
            return

        def on_connection(server, error):
            client = pyuv.TCP(server.loop)
            server.accept(client)
            clients.append(client)
            client.start_read(on_read)

        def signal_cb(handle, signum):
            signal_h.close()
            server.close()

        loop = pyuv.Loop.default_loop()
        clients = []

        server = pyuv.TCP(loop)
        server.bind((self.host, self.port))
        server.listen(on_connection)

        signal_h = pyuv.Signal(loop)
        signal_h.start(signal_cb, signal.SIGINT)

        loop.run()   
        print("Server on " + self.host + " at port " + str(self.port) + " has stopped.")



