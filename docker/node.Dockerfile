FROM node:20.14.0-bookworm

RUN npm install -g typescript@5.4.5

WORKDIR /workspace
