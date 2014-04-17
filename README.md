pythonREST
==========

Simple RESTful python interface for calling functions on a server instance. The main code is all contained within two classes in `pythonrest.py`. A working example is contained in `example.py`.

I have tested the code in: *Python 2.7.6 :: Anaconda 1.9.1 (x86_64)*; the only additional module you should need is pyuv, which can be downloaded via `pip install pyuv`.

To run the example first call the following in one terminal window:

```
python example.py
```

Then, in another window place the following PUSH request:

```
curl -X PUSH http://0.0.0.0:9090 -d '{"fun": "root_fun", "params" : {"n" : 10}}'
```

The square root of 10 should be returned. You can change the value of n to calculate other square roots as well as change the *root_fun* to *square_fun* to calculate squares.
