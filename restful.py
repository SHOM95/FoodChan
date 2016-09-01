from flask import Flask, jsonify, request, render_template   #import objects from the Flask model
app = Flask(__name__)   #define app using Flask

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})
@app.route('/home',methods=['GET'])
def home():
    return 'This page is home page'



if __name__ == '__main__':
    app.run(debug=True, port=8080)  #run app on port 8080 in debug mode


