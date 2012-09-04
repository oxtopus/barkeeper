from functools import partial
import json
from kazoo.client import KazooClient
from flask import Flask, make_response, Response
import zookeeper

app = Flask(__name__)

encode = partial(json.dumps, indent=2)

def error_response(reason, status, *args):
    response = {
        'reason': response,
        'status': status
    }
    return make_response(encode(response), status, *args)

def normalize_path(path):
    return '/' + '/'.join(filter(None, path.split('/')))    

@app.route('/favicon.ico')
def favicon():
    return ""
    
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    node = normalize_path(path)
    try:
        value, znode = zk.get(node)

        if znode.numChildren > 0:
            children = zk.get_children(node)
        else:
            children = []

        return Response(
            encode([value, znode._asdict(), children]), \
            content_type='application/json')

    except zookeeper.NoNodeException:
        return error_response('Not found', 404)
    
    except Exception as e:
        return error_response(str(e), 500)

if __name__ == "__main__":
    zk = KazooClient()
    zk.start()
    app.run()