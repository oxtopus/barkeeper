barkeeper
=========

Barkeeper is a lightweight [Flask](http://flask.pocoo.org/)-based web application to provide a REST 
interface to [Apache ZooKeeper](http://zookeeper.apache.org/).  URL paths are translated to ZooKeeper node 
paths, and responses are JSON-formatted.

Responses are 3-tuples comprising:

- Node data
- ZNode metadata
- List of node children

Usage
-----

Start barkeeper

<pre>python -m barkeeper.app</pre>

Make HTTP GET requests

<pre>curl http://localhost:5000</pre>

Response for "/":

<pre>[
  "", 
  {
    "aversion": 0, 
    "ctime": 0, 
    "cversion": 0, 
    "czxid": 0, 
    "dataLength": 0, 
    "ephemeralOwner": 0, 
    "mtime": 0, 
    "mzxid": 0, 
    "numChildren": 1, 
    "pzxid": 0, 
    "version": 0
  }, 
  [
    "zookeeper"
  ]
]</pre>

<pre>curl http://localhost:5000/zookeeper</pre>

Response for "/zookeeper"

<pre>[
  "", 
  {
    "aversion": 0, 
    "ctime": 0, 
    "cversion": 0, 
    "czxid": 0, 
    "dataLength": 0, 
    "ephemeralOwner": 0, 
    "mtime": 0, 
    "mzxid": 0, 
    "numChildren": 1, 
    "pzxid": 0, 
    "version": 0
  }, 
  [
    "quota"
  ]
]</pre>

Currently, only GET is supported.

&copy; 2012 Austin Marshall