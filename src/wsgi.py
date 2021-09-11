from backend import flask_app
from backend.ConversionTool.entry_point import HelloThere, UploadFile
from flask_restful import Api


api = Api(flask_app)

api.add_resource(HelloThere, "/")

api.add_resource(UploadFile, "/upload")

if __name__ == "__main__":
    flask_app.run(debug=True, port=5001)
