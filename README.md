# docker-ci-cd

Roda testes
docker run -it --rm -v "$PWD":/usr/src/app -w /usr/src/app python:3 python -m unittest

Integração continua e entrega continua com Docker.

## Conceitos

Registry

## No circle

Defina a imagem a ser utilizada nos jobs.

Você pode defini mais de uma imagem para os jobs (como banco de dados).

Para o deploy, puxe a imagem pro Heroku registry.

## No Heroku

Você pode usar os comandos

heroku container:push web

E tem outras coisas para customizar essas imagens no heroku registry.
