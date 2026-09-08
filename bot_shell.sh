#!/bin/bash

# ⚡ BOT SHELL SYSTEM

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Variáveis do bot
BOT_START_TIME=$(date +%s)
BOT_NAME="BotShell"
VERSION="1.0.0"

# Função para mostrar o banner
show_banner() {
    echo -e "${CYAN}╭━━━━━━━━━━━━━━━━━━━━━━╮${NC}"
    echo -e "${CYAN}┃   ⚡ BOT SHELL SYSTEM ┃${NC}"
    echo -e "${CYAN}╰━━━━━━━━━━━━━━━━━━━━━━╯${NC}"
    echo ""
}

# Função /echo
cmd_echo() {
    local mensagem="$*"
    if [ -z "$mensagem" ]; then
        echo -e "${RED}❌ Erro: Nenh mensagem fornecida${NC}"
        return 1
    fi
    echo -e "${GREEN}📢 $mensagem${NC}"
}

# Função /status
cmd_status() {
    echo -e "${CYAN}📊 STATUS DO BOT${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    echo -e "🤖 Bot: ${BOT_NAME}"
    echo -e "📦 Versão: ${VERSION}"
    echo -e "🟢 Estado: Online"
    echo -e "⏰ Uptime: $(get_uptime)"
    echo -e "💻 Sistema: $(uname -s) $(uname -m)"
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /uptime
cmd_uptime() {
    local uptime_seconds=$(( $(date +%s) - BOT_START_TIME ))
    local days=$(( uptime_seconds / 86400 ))
    local hours=$(( (uptime_seconds % 86400) / 3600 ))
    local minutes=$(( (uptime_seconds % 3600) / 60 ))
    local seconds=$(( uptime_seconds % 60 ))
    
    echo -e "${CYAN}⏰ TEMPO DE ATIVIDADE${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    if [ $days -gt 0 ]; then
        echo -e "${days}d ${hours}h ${minutes}m ${seconds}s"
    elif [ $hours -gt 0 ]; then
        echo -e "${hours}h ${minutes}m ${seconds}s"
    elif [ $minutes -gt 0 ]; then
        echo -e "${minutes}m ${seconds}s"
    else
        echo -e "${seconds}s"
    fi
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /info
cmd_info() {
    echo -e "${CYAN}ℹ️  INFORMAÇÕES DO SISTEMA${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    echo -e "🤖 Bot: ${BOT_NAME} v${VERSION}"
    echo -e "💻 SO: $(cat /etc/os-release 2>/dev/null | grep PRETTY_NAME | cut -d'"' -f2 || uname -s)"
    echo -e "🖥️  Kernel: $(uname -r)"
    echo -e "📊 Arquitetura: $(uname -m)"
    echo -e "👤 Usuário: $(whoami)"
    echo -e "📁 Direório: $(pwd)"
    echo -e "🔗 Shell: $SHELL"
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /ls
cmd_ls() {
    echo -e "${CYAN}📂 ARQUIVOS PERMITIDOS${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    if [ -e "/workspace" ]; then
        ls -la /workspace 2>/dev/null || echo -e "${RED}❌ Erro ao listar /workspace${NC}"
    else
        ls -la
    fi
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /pwd
cmd_pwd() {
    echo -e "${CYAN}📁 DIRETÓRIO ATUAL${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    echo -e "${BLUE}$(pwd)${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /ping
cmd_ping() {
    echo -e "${CYAN}📶 VERIFICANDO LATÊNCIA...${NC}"
    local start=$(date +%s%N)
    # Simular uma resposta
    sleep 0.1
    local end=$(date +%s%N)
    local duration=$(( (end - start) / 1000000 ))
    
    echo -e "${YELLOW}──────────────────────${NC}"
    echo -e "🟢 Pong! Latência: ${duration}ms"
    echo -e "${YELLOW}──────────────────────${NC}"
}

# Função /help
cmd_help() {
    show_banner
    echo -e "${CYAN}📚 COMANDOS DISPONÍVEIS${NC}"
    echo -e "${YELLOW}──────────────────────${NC}"
    echo -e "${MAGENTA}📢 COMUNICAÇÃO${NC}"
    echo -e "  ${GREEN}/echo <mensagem>${NC} - Envia uma mensagem personalizada"
    echo ""
    echo -e "${MAGENTA}🖥️ SISTEMA${NC}"
    echo -e "  ${GREEN}/status${NC} - Mostra o status do bot"
    echo -e "  ${GREEN}/uptime${NC} - Mostra há quanto tempo está online"
    echo -e "  ${GREEN}/info${NC} - Informações do sistema"
    echo -e "  ${GREEN}/ls${NC} - Lista arquivos do diretório"
    echo -e "  ${GREEN}/pwd${NC} - Mostra o diretório atual"
    echo -e "  ${GREEN}/ping${NC} - Verifica latência"
    echo -e "  ${GREEN}/help${NC} - Mostra esta ajuda"
    echo -e "${YELLOW}──────────────────────${NC}"
}

get_uptime() {
    local uptime_seconds=$(( $(date +%s) - BOT_START_TIME ))
    local days=$(( uptime_seconds / 86400 ))
    local hours=$(( (uptime_seconds % 86400) / 3600 ))
    local minutes=$(( (uptime_seconds % 3600) / 60 ))
    local seconds=$(( uptime_seconds % 60 ))
    
    if [ $days -gt 0 ]; then
        echo "${days}d ${hours}h ${minutes}m ${seconds}s"
    elif [ $hours -gt 0 ]; then
        echo "${hours}h ${minutes}m ${seconds}s"
    elif [ $minutes -gt 0 ]; then
        echo "${minutes}m ${seconds}s"
    else
        echo "${seconds}s"
    fi
}

# Loop principal
show_banner
echo -e "${GREEN}BotShell v${VERSION} iniciado!${NC}"
echo -e "Digite ${CYAN}/help${NC} para ver os comandos disponíveis."
echo ""

while true; do
    echo -ne "${CYAN}${BOT_NAME}> ${NC}"
    read -r input
    
    if [ -z "$input" ]; then
        continue
    fi
    
    if [[ "$input" == /* ]]; then
        cmd="${input%% *}"
        cmd="${cmd#/}"
        arg="${input#*/ }"
        
        case "$cmd" in
            echo)
                cmd_echo "$arg"
                ;;
            status)
                cmd_status
                ;;
            uptime)
                cmd_uptime
                ;;
            info)
                cmd_info
                ;;
            ls)
                cmd_ls
                ;;
            pwd)
                cmd_pwd
                ;;
            ping)
                cmd_ping
                ;;
            help)
                cmd_help
                ;;
            sair|exit)
                echo -e "${RED}Encerrando ${BOT_NAME}...${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Comando desconhecido: /$cmd${NC}"
                echo -e "   Digite /help para ver os comandos disponíveis."
                ;;
        esac
    else
        echo -e "${RED}❌ Comandos devem começar com /${NC}"
    fi
done