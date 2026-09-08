# 🤖 Discord Bot com WebSocket Custom

Bot Discord que conecta **diretamente na Gateway WebSocket** sem usar libs como `discord.py` ou `hikari`. Implementação pura usando `websockets` + zlib.

## ✨ Features

- Conexão WebSocket direta com a Gateway do Discord (v10)
- Compressão zlib-stream nativa
- Heartbeat automático com tratamento de ACK
- Resume de sessão em reconexões (op 6)
- Reconexão automática com backoff exponencial
- Intents: GUILDS + GUILD_MESSAGES (513)
- Envio de mensagens via REST API com `urllib` (zero dependências HTTP)

## 📦 Instalação

```bash
pip install -r requirements.txt
cp .env.example .env
# edite o .env e coloque seu token
```

## 🔑 Token

1. Vá em https://discord.com/developers/applications
2. Crie uma application → Bot → copie o token
3. Habilite o **Message Content Intent** em Bot → Privileged Gateway Intents
4. Convide o bot pro seu servidor com permissão de `Send Messages`

## 🚀 Rodar

```bash
python bot.py
```

## 💬 Comandos

| Comando | O que faz |
|---|---|
| `!ping` | responde Pong |
| `!help` | lista comandos |
| `!info` | info do bot |
| `!echo <texto>` | repete seu texto |
| `!time` | hora atual |

## 🧠 Como funciona

```
client  ──▶  wss://gateway.discord.gg  (Hello)
client  ──▶  op 2 Identify
server  ──▶  op 11 Heartbeat ACK
client  ──▶  op 1 Heartbeat (loop a cada 41.25s)
server  ──▶  t READY
server  ──▶  t MESSAGE_CREATE  (eventos)
client  ──▶  POST /channels/{id}/messages  (REST pra enviar)
```

## 🛠 Estrutura

- `bot.py` — código principal (gateway + handlers + REST)
- `requirements.txt` — dependências
- `.env.example` — template do token

## 📝 Notas

- O envio de mensagem usa a REST API do Discord via `urllib` (stdlib), mantendo o bot 100% puro em dependências externas (só `websockets` pro WS).
- A compressão `zlib-stream` é suportada nativamente pela stdlib.
- Intents mínimo: 513 (1 + 512). Ative o Message Content Intent no portal pra ler conteúdo de mensagens.