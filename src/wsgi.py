from backend import fast_app
from backend.ConversionTool.entry_point import HelloThere, UploadFile
from flask_restful import Api


api = Api(fast_app)

api.add_resource(HelloThere, "/")

api.add_resource(UploadFile, "/upload")

if __name__ == "__main__":
    fast_app.run(debug=True, port=5001)
