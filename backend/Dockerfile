FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install fastapi pymysql uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
