FROM python:2-alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY static ./static
COPY templates ./templates
COPY main.py ./
CMD [ "python", "main.py" ]