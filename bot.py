# Bot de Discord com WebSocket Custom

Implementação pura de cliente Discord usando `websockets` + zlib, sem `discord.py` nem `hikari`.

Conecta diretamente na Gateway WebSocket do Discord (v10), trata heartbeat, resume sessão e envia mensagens via REST API com `urllib`.

## Instalação

```bash
pip install -r requirements.txt
cp .env.example .env
# edite o .env com seu token
```

## Uso

```bash
python bot.py
```

## Comandos

- `!ping` — Pong
- `!help` — ajuda
- `!info` — info do bot
- `!echo <texto>` — ecoa
- `!time` — hora atual

## Estrutura

- `bot.py` — código principal (gateway, handlers, REST)
- `bot_shell.py` — variante com shell integrado
- `bot_demo.sh` / `bot_shell.sh` — scripts de demo/launch
- `browser_bot.py` / `browser_bot_v2.py` — variantes com navegador
- `requirements.txt` — dependências
- `.env.example` — template do token