#!/usr/bin/env python3
"""
⚡ BOT SHELL SYSTEM - Python Implementation
"""

import os
import time
import platform
import datetime

# Cores para output
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
MAGENTA = '\033[0;35m'
CYAN = '\033[0;36m'
NC = '\033[0m'  # No Color

# Variáveis do bot
BOT_START_TIME = time.time()
BOT_NAME = "BotShell"
VERSION = "1.0.0"

def get_uptime():
    uptime_seconds = int(time.time() - BOT_START_TIME)
    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def show_banner():
    print(f"{CYAN}╭━━━━━━━━━━━━━━━━━━━━━━╮{NC}")
    print(f"{CYAN}┃   ⚡ BOT SHELL SYSTEM ┃{NC}")
    print(f"{CYAN}╰━━━━━━━━━━━━━━━━━━━━━━╯{NC}")
    print()

def cmd_echo(mensagem):
    if not mensagem:
        print(f"{RED}❌ Erro: Nenhagem mensagem fornecida{NC}")
        return
    print(f"{GREEN}📢 {mensagem}{NC}")

def cmd_status():
    print(f"{CYAN}📊 STATUS DO BOT{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    print(f"🤖 Bot: {BOT_NAME}")
    print(f"📦 Versão: {VERSION}")
    print(f"🟢 Estado: Online")
    print(f"⏰ Uptime: {get_uptime()}")
    print(f"💻 Sistema: {platform.system()} {platform.machine()}")
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_uptime():
    print(f"{CYAN}⏰ TEMPO DE ATIVIDADE{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    print(get_uptime())
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_info():
    print(f"{CYAN}ℹ️  INFORMAÇÕES DO SISTEMA{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    print(f"🤖 Bot: {BOT_NAME} v{VERSION}")
    
    # Tentar obter info do SO
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('PRETTY_NAME='):
                    pretty_name = line.split('=')[1].strip().strip('"')
                    print(f"💻 SO: {pretty_name}")
                    break
    except:
        print(f"💻 SO: {platform.system()}")
    
    print(f"🖥️  Kernel: {platform.release()}")
    print(f"📊 Arquitetura: {platform.machine()}")
    print(f"👤 Usuário: {os.getenv('USER', 'unknown')}")
    print(f"📁 Direório: {os.getcwd()}")
    print(f"🔗 Shell: {os.getenv('SHELL', 'python')}")
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_ls():
    print(f"{CYAN}📂 ARQUIVOS PERMITIDOS{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    try:
        files = os.listdir('.')
        for f in sorted(files):
            stat = os.stat(f)
            size = stat.st_size
            print(f"  {f} ({size} bytes)")
    except Exception as e:
        print(f"{RED}❌ Erro ao listar: {e}{NC}")
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_pwd():
    print(f"{CYAN}📁 DIRETÓRIO ATUAL{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    print(f"{BLUE}{os.getcwd()}{NC}")
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_ping():
    print(f"{CYAN}📶 VERIFICANDO LATÊNCIA...{NC}")
    start = time.time()
    time.sleep(0.1)
    end = time.time()
    duration = int((end - start) * 1000)
    
    print(f"{YELLOW}──────────────────────{NC}")
    print(f"🟢 Pong! Latência: {duration}ms")
    print(f"{YELLOW}──────────────────────{NC}")

def cmd_help():
    show_banner()
    print(f"{CYAN}📚 COMANDOS DISPONÍVEIS{NC}")
    print(f"{YELLOW}──────────────────────{NC}")
    print(f"{MAGENTA}📢 COMUNICAÇÃO{NC}")
    print(f"  {GREEN}/echo <mensagem>{NC} - Envia uma mensagem")
    print("")
    print(f"{MAGENTA}🖥️ SISTEMA{NC}")
    print(f"  {GREEN}/status{NC} - Mostra o status do bot")
    print(f"  {GREEN}/uptime{NC} - Mostra há quanto tempo está online")
    print(f"  {GREEN}/info{NC} - Informações do sistema")
    print(f"  {GREEN}/ls{NC} - Lista arquivos do diretório")
    print(f"  {GREEN}/pwd{NC} - Mostra o diretório atual")
    print(f"  {GREEN}/ping{NC} - Verifica latência")
    print(f"  {GREEN}/help{NC} - Mostra esta ajuda")
    print(f"{YELLOW}──────────────────────{NC}")

def main():
    show_banner()
    print(f"{GREEN}BotShell v{VERSION} iniciado!{NC}")
    print(f"Digite {CYAN}/help{NC} para ver os comandos disponíveis.")
    print()
    
    while True:
        try:
            user_input = input(f"{CYAN}{BOT_NAME}>{NC} ").strip()
            
            if not user_input:
                continue
            
            if user_input.startswith('/'):
                parts = user_input[1:].split(' ', 1)
                cmd = parts[0].lower()
                arg = parts[1] if len(parts) > 1 else ""
                
                if cmd == 'echo':
                    cmd_echo(arg)
                elif cmd == 'status':
                    cmd_status()
                elif cmd == 'uptime':
                    cmd_uptime()
                elif cmd == 'info':
                    cmd_info()
                elif cmd == 'ls':
                    cmd_ls()
                elif cmd == 'pwd':
                    cmd_pwd()
                elif cmd == 'ping':
                    cmd_ping()
                elif cmd == 'help':
                    cmd_help()
                elif cmd == 'sair' or cmd == 'exit':
                    print(f"{RED}Encerrando {BOT_NAME}...{NC}")
                    break
                else:
                    print(f"{RED}❌ Comando desconhecido: /{cmd}{NC}")
                    print(f"   Digite /help para ver os comandos disponíveis.")
            else:
                print(f"{RED}❌ Comandos devem começar com /{NC}")
        
        except KeyboardInterrupt:
            print(f"\n{RED}Encerrando {BOT_NAME}...{NC}")
            break
        except Exception as e:
            print(f"{RED}❌ Erro: {e}{NC}")

if __name__ == "__main__":
    main()