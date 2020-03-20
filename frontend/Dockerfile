FROM node:12.16-alpine as build

WORKDIR /code

COPY . /code

RUN apk add -U yarn && \
    yarn install && \
    yarn build

FROM nginx:alpine
