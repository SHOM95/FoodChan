from flask import Flask, jsonify, request   #import objects from the Flask model
app = Flask(__name__)   #define app using Flask

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)  #run app on port 8080 in debug mode

