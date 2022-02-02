from backend import fast_app as app
from backend.ConversionTool.utils import process_file
from fastapi import File


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
