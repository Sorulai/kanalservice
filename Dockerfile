FROM python:latest
WORKDIR /script
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip
COPY ./requirements.txt /script/
RUN pip install -r requirements.txt
COPY . /script/
CMD ["python", "-u", "main.py"]
