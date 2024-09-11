# challenge-numbers
Esse projeto é uma implementação de uma API para realizar operações matemáticas com números.

## Requisitos
- [ ] Implemente uma API que permita realizar soma e média de uma lista de números inteiros.
- [ ] Escrever testes unitários para a API.
- [ ] Escrever documentação para a API.
- [ ] Escrever um README para o projeto.

## Versão
1.0.0

## Executar aplicação
```bash
  docker-compose up -d
```
## Executar testes
```bash
   docker-compose exec web poetry run pytest
```
## Documentação
acessar: http://localhost:8000/docs / http://localhost:8000/redoc


## Curls de teste
Soma de uma lista de números
```bash
curl --location 'http://localhost:8000/sum' \
--header 'Content-Type: application/json' \
--data '{
  "numbers": [
    10,
    20
  ]
}'
```

Média de uma lista de números
```bash
curl --location 'http://localhost:8000/average' \
--header 'Content-Type: application/json' \
--data '{
  "numbers": [
    10,
    20
  ]
}'
```