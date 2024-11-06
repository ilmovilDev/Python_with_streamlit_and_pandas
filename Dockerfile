FROM python:3.13-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8501"]
# CMD [ "python", "main.py" ]

