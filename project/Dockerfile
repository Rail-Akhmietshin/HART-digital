FROM python:3.11.1-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/project


RUN pip install --upgrade pip

COPY . .

COPY ./req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/project/wheels -r req.txt



FROM python:3.11.1-alpine


RUN mkdir -p /home/project



ENV HOME=/home/project
ENV APP_HOME=/home/project/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

COPY --from=builder /usr/src/project/wheels /wheels
COPY --from=builder /usr/src/project/req.txt .
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME