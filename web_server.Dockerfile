FROM node:18-alpine
#18 은 node.js 의 version 을 맞추기 위해서 node -v 의 결과와 동일하도록 셋팅

WORKDIR /

COPY .idea ./
COPY .venv ./
COPY config ./
COPY models ./
COPY python_pakage_version.log ./
# COPY run_development_server.ini ./
COPY static ./
COPY templates ./
COPY name ./
COPY web_flask.py ./
# COPY web_server.Dockerfile ./
COPY __pycache__ ./

# CMD ["python web_flask.py"]
ENTRYPOINT ["python", "web_flask.py"] 