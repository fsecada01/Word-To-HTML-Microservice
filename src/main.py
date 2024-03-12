from fastapi import File

# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

from backend import get_app
from backend.ConversionTool.core import convert_to_format
from backend.ConversionTool.utils import process_file
from backend.settings import app_settings

# origins = [
#     "http://127.0.0.1:5000",
#     "http://127.0.0.1:8000",
#     "http://localhost:5000",
#     "http://localhost:8000",
#     "https://e6dmdc.deta.dev",
#     "https://deta.space",
#     "https://winword_html-1-r7596704.deta.app",
#     "https://www.adc44.org",
#     "https://adc44.org",
#     "https://rankedjobs.com",
# ]

fast_app = get_app(settings_inst=app_settings)


# fast_app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "PUT"],
#     allow_headers=["*"],
# )


@fast_app.get("/")
async def greeting():
    return {
        "message": "Hello! Thanks for visiting. Please upload your "
        "Microsoft Word file to /upload. Thanks!"
    }


# @app.route("/upload", methods=["GET", "POST", "PUT"])
# async def convert_document(file: UploadFile, request: Request or None):
# print(methods)
@fast_app.put("/upload")
async def convert_document(file: bytes = File(...), type_name: str = "html"):
    if file:
        html_content = process_file(file, type_name=type_name)
        return {"data": html_content}
    else:
        return {"data": "Waiting on a file from you!"}


@fast_app.post("/convert")
async def convert_string(str_or_html: str, type_name: str = "html"):
    if str_or_html:
        html_content = convert_to_format(
            content=str_or_html, type_name=type_name
        )

        return {"data": html_content}
    else:
        return {"data": "Waiting on a string from you!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:fast_app", host="0.0.0.0", reload=True, port=5001)
