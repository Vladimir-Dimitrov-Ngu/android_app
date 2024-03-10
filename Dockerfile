FROM python:3.11

COPY backend /app/backend
COPY frontend /app/frontend
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
COPY weights /app/weights


RUN pip install --no-cache-dir -r /app/requirements.txt
RUN chmod -R 755 /app

WORKDIR /app


EXPOSE 9000
EXPOSE 9001
EXPOSE 9002


CMD ["python", "main.py"]
