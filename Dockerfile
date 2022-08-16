FROM python:3.7-slim

WORKDIR /auth

COPY . /auth

EXPOSE 8001

RUN pip install -r requirements.txt


CMD ["uvicorn","src.main:app","--reload","--port=8001","--host=0.0.0.0" ]



