# Microsoft Word to HTML Microservice

This is a build for a microservice built with flask-restful. The idea is to upload Microsoft Word files via put request and receive a JSON payload containing HTML string. The process is fairly simple.

1. Take your word file
2. Make a put request with the files argument and a keyword argument for the
   name of the file type (i.e.: `type_name`). Current choices are `html` and
   `markdown`
3. Parse the JSON payload to extract the converted HTML content.

Example
```
import requests

url = 'http://localhost:5000/upload'  # change this to your server address or AWS lamdba URI
word_file = 'foo_bar.docx'
type_name = "html"
files = {
    'file': open(word_file, 'rb')
}

params = {"type_name": type_name}

r = requests.put(url, params=params, files=files)
resp = r.json()

html = resp.get('data')

```

CURL example
```
$ curl http://localhost:5000/upload?type_name=html -F "file=foo_bar.docx" -X PUT
```
