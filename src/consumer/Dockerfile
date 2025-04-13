FROM python:3.12-slim
WORKDIR /app
COPY main.py .
RUN pip install kafka-python
CMD ["python", "-u", "main.py"]