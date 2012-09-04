barkeeper
=========

Barkeeper is a lightweight [Flask](http://flask.pocoo.org/)-based web 
application to provide a REST interface to 
[Apache ZooKeeper](http://zookeeper.apache.org/).  URL paths are translated to ZooKeeper node paths, and responses are JSON-formatted.

A note aboute trailing slashes:

> znodes are synonymous with both files and directories within a heirarchical
> file system.  Barkeeper distinguishes requests for znodes and znode children
> by inspecting the url path for a trailing slash.  A request for a node with a
trailing slash will be interpreted as a request for the list of children for 
that node.  See below for examples.

Usage
-----

Start barkeeper

<pre>python -m barkeeper.app</pre>

Make HTTP GET requests

<pre>curl http://localhost:5000</pre>

<pre>[
  "zookeeper"
]</pre>

<pre>curl http://localhost:5000/zookeeper</pre>

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
  }
]</pre>

<pre>curl http://localhost:5000/zookeeper/</pre>

<pre>[
  "quota"
]</pre>


Currently, only GET is supported.

&copy; 2012 Austin Marshall