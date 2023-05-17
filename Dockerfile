FROM alpine:latest
LABEL authors="jk"
RUN apk add --no-cache python3 py3-pip && \
    pip3 install --upgrade pip
WORKDIR /app
COPY ./dist/*.whl ./.env ./requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt /app/*.whl

ENTRYPOINT ls -Flah && helpy-discord-bot