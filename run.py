from flask import Flask, request
from flask_restful import Resource, Api

import markdown

app = Flask(__name__)

api = Api(app)

@app.route("/")
def start():
    return markdown.markdownFromFile("README.md")

class GuessGender(Resource):
    def get(self):
        response = 'Hi. Let me guess your gender by giving me your name.'

        return {'responseCode': '000', 'message': response}, 200

    def post(self):
        name = request.json['name']

        response = name + '? Sounds female.'

        return {'responseCode': '000', 'message': response}, 201

api.add_resource(GuessGender, '/guessgender')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
