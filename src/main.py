import html
from typing import Literal

from fastapi import File, Form

from backend import get_app
from backend.consts import delim_tab
from backend.ConversionTool.utils import process_file, str_conversion
from backend.settings import app_settings

fast_app = get_app(settings_inst=app_settings)


@fast_app.get("/")
async def greeting():
    return {
        "message": "Hello! Thanks for visiting. Please upload your "
        "Microsoft Word file to /upload. Thanks!"
    }


@fast_app.put("/upload")
async def convert_document(file: bytes = File(...), type_name: str = "html"):
    if file:
        html_content = process_file(file, type_name=type_name)
        return {"data": html_content}
    else:
        return {"data": "Waiting on a file from you!"}


@fast_app.post("/convert")
async def convert_string(
    str_or_html: str = Form(...),
    type_name: Literal["html", "markdown", "text"] = "html",
):
    if str_or_html:
        if type_name in ("text", "markdown"):
            html_content = str_conversion(
                content=str_or_html, type_name=type_name
            )
        else:
            # html_content = html.unescape(str_or_html)
            print(str_or_html)
            html_content = str_or_html
            html_content = html.escape(html_content)
            for k, v in delim_tab.items():
                html_content = html_content.replace(v, k)

        return {"data": html_content}
    else:
        return {"data": "Waiting on a string from you!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:fast_app", host="0.0.0.0", reload=True, port=5001)
