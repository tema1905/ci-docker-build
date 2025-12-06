FROM python:3.10-slim

WORKDIR /app

COPY AllFrames.py /app/

CMD ["python", "AllFrames.py"]
