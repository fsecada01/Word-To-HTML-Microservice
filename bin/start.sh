#!/bin/bash

__dir="$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
cd ${__dir}/.. || exit
source .venv/bin/activate
cd src || exit
# python -m backend.utils
gunicorn main:fast_app -w 4 -k uvicorn.workers.UvicornWorker \
--forwarded-allow-ips "*" \
-b 0.0.0.0:"${PORT}"
