from fastapi import File
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

from backend import fast_app as app
from backend.ConversionTool.utils import process_file

origins = [
    "http://127.0.0.1:5000",
    "http://localhost:5000",
    "https://e6dmdc.deta.dev/",
    "https://www.adc44.org",
    "https://adc44.org",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "PUT"],
    allow_headers=["*"],
)


@app.get("/")
async def greeting():
    return {
        "message": "Hello! Thanks for visiting. Please upload your "
        "Microsoft Word file to /upload. Thanks!"
    }


# @app.route("/upload", methods=["GET", "POST", "PUT"])
# async def convert_document(file: UploadFile, request: Request or None):
# print(methods)
@app.put("/upload")
async def convert_document(file: bytes = File(...)):
    if file:
        html_content = process_file(file)
        return {"data": html_content}
    else:
        return {"data": "Waiting on a file from you!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, debug=True, port=5001)
