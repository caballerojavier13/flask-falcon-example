from flask import Flask,Response, request
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def json_keys():
    if request.method == 'POST':
        data = json.loads(request.data.decode("utf-8"))
        data['keys'] = [key for key in data]

        body = json.dumps(data)
        resp = Response(response=body,
                        status=200,
                        mimetype="application/json")        
        return resp
    else:
        return "POST a JSON body to get its keys"

if __name__ == "__main__":
    app.run()