from flask import Flask, request, jsonify
from API_script import my_function

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    param = request.args.get('param')
    result = my_function(param)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/api?param=World