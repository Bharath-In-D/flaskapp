# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class Index(Resource):
  def index(self):
    print("Hello Bharath")
    return jsonify({'message':"Bharath"})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')


# driver function
if __name__ == '__main__':

	app.run(debug = True)
