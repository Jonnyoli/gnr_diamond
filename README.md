# Backend Flask para Registro de Serviço

Este projeto é uma API simples em Flask que recebe dados de um bot do Discord e responde com uma confirmação.

## Como usar

1. Faça o deploy no [Render](https://render.com) ou outro serviço compatível.
2. Configure o bot do Discord para enviar requisições POST para a URL:

```
https://seu-app.onrender.com/registrar_servico
```

## Estrutura esperada do JSON:

```
{
  "usuario": "João",
  "entrada": "2025-07-19 14:30:00",
  "saida": "2025-07-19 18:00:00",
  "duracao_servico": "3:30:00"
}
```