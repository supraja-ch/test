from flask import Flask,request,jsonify
import io, os, json
import pandas as pd

app = Flask(__name__)

@app.route('/readfile',methods=['GET'])
def readfile():
    inputfile = request.files['inputfile']
    input_id = request.args.get('input_id')
    data = pd.read_excel(inputfile,encoding="ISO-8859-1")
    json_data = data.to_dict(orient='records')
    json_data = json_data[:int(input_id)]
    return jsonify({"status":True,"res":json_data})

@app.route('/search_readfile',methods=['GET'])
def search_readfile():

    inputfile = request.files['inputfile']
    input_search = request.form['input_search']
    data = pd.read_excel(inputfile,encoding="ISO-8859-1")
    json_data = data.to_dict(orient='records')
    # import pdb;
    # pdb.set_trace()
    jsn = json.loads(input_search)
    key, value = list(jsn.keys())[0], list(jsn.values())[0]
    response = []
    columns = []

    for g in json_data:
        if key in g:
            columns.append(key)
            if value == g[key]:
                response.append(g)
    if not columns:
        return jsonify({"status":False,"message":"no columns are available"})
    if response:
        return jsonify({"status":True,"res":response})
    else:
        return jsonify({"status":False,"message":response})

if __name__ == '__main__':
   app.run(debug = True)