import json
from flask import Flask, jsonify, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/sum', methods=['POST'])
def post_sum():
    data = request.get_json()
    print(data)
    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Please provide both num1 and num2'}), 400
    try:
        # conversion of number.
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        return jsonify({'sum':num1+num2}), 200

    except ValueError:
        return jsonify({'error': 'Please provide valid numbers'}), 400

if __name__ == '__main__':
   app.run(port=5000)