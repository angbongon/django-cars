FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN adduser -D user
USER user

ENV PORT=8000

EXPOSE 8000

CMD ["python" , "manage.py", "runserver"]