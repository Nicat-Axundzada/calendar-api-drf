FROM python:3.12.2-alpine3.19
LABEL maintainer="Nijat Akhundzada"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
RUN mkdir /calendar_api
COPY ./calendar_api /calendar_api/
WORKDIR /calendar_api
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user