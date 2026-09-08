#!/usr/bin/env python3
"""
✨ BrowserBot - Um bot que controla o navegador (Chrome no Cloud)
⛏️ Baseado em automação de navegadores via Chromium na nuvem

Funcionalidades:
- Navegação para URLs
- Cliques em elementos
- Preenchimento de campos
- Extração de texto e elementos
- Captura de tela
- Status do bot

Requisitos:
- Internet conectado (accesso ao navegador em nuvem)
"""

import sys
import os
import time
from urllib.parse import urljoin, urlparse

# Importamos a ferramenta de navegador embutida
# (browser_use) para controle real de Chrome

try:
    from browser_use import Browser, Page
    BROWSER_AVAILABLE = True
except ImportError:
    BROWSER_AVAILABLE = False
    print("⚠️  browser_use não encontrado. O bot terá limitações.")


class BrowserBot:
    """Bot que controla o navegador remoto."""

    def __init__(self, name="BrowserBot"):
        self.name = name
        self.browser = None
        self.page = None
        self._initialized = False

    def initialize(self):
        """Inicializa o bot e o navegador."""
        if not BROWSER_AVAILABLE:
            print("❌ Erro: Não é possível inicializar o BrowserBot.")
            print("   Certifique-se de que o navegador em nuvem está funcionando.")
            return False

        # Cria o navegador e a página
        self.browser = Browser()
        self.page = self.browser.page
        
        # Configurações padrão
        self.browser.set_window_title(self.name)
        print(f"✅ {self.name} iniciado!")
        return True

    def go_to(self, url, wait=10):
        """Abra uma URL no navegador."""
        if not self.browser:
            print("❌ Erro: Nenhum navegador inicializado.")
            return False
        try:
            self.page.goto(url, wait=wait)
            print(f"🌐 Navegando para: {url}")
            return True
        except Exception as e:
            print(f"❌ Erro ao navegar para {url}: {e}")
            return False

    def click(self, selector, timeout=10):
        """Clique em um elemento pelo seletor CSS."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return False
        try:
            elements = self.page.evaluate_css_selector(selector)
            if not elements:
                print(f"❌ Nenhum elemento encontrado com seletor: {selector}")
                return False
            # Clica no primeiro elemento
            self.page.click(elements[0])
            print(f"✋ Clicou em: {elements[0].outerHTML[:200]}...")
            return True
        except Exception as e:
            print(f"❌ Erro ao clicar: {e}")
            return False

    def type(self, selector, text, timeout=10):
        """Digite texto em um campo pelo seletor."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return False
        try:
            elements = self.page.evaluate_css_selector(selector)
            if not elements:
                print(f"❌ Nenhum elemento encontrado com seletor: {selector}")
                return False
            self.page.type(elements[0], text)
            print(f"💬 Digiteu '{text}' no campo {selector}")
            return True
        except Exception as e:
            print(f"❌ Erro ao digitar: {e}")
            return False

    def fill_form(self, fields, values):
        """Preencha múltiplos campos de um formulário."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return False
        success = True
        for i, (field, value) in enumerate(zip(fields, values)):
            try:
                self.page.fill(field, value)
                print(f"✅ Preenchedo campo {i+1}: {field} -> {value}")
            except Exception as e:
                print(f"❌ Falha ao preencher campo {i+1}: {e}")
                success = False
        return success

    def screenshot(self, filename="screenshot.png"):
        """Tira uma captura de tela."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return False
        try:
            self.page.screenshot(filename)
            print(f"📸 Screenshot salva em: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erro ao tirar screenshot: {e}")
            return False

    def get_title(self):
        """Obtém o título da página atual."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return None
        try:
            title = self.page.evaluate("document.title")
            return title
        except Exception as e:
            print(f"❌ Erro ao obter título: {e}")
            return None

    def get_text(self, selector=None):
        """Extrai texto da página ou de um elemento."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return None
        try:
            if selector:
                elements = self.page.evaluate_css_selector(selector)
                if elements:
                    return elements[0].text_content()
                return None
            else:
                return self.page.evaluate("document.body.innerText")
        except Exception as e:
            print(f"❌ Erro ao extrair texto: {e}")
            return None

    def get_elements(self, selector):
        """Lista elementos que combinam com o seletor."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return []
        try:
            elements = self.page.evaluate_css_selector(selector)
            return elements
        except Exception as e:
            print(f"❌ Erro ao buscar elementos: {e}")
            return []

    def execute_js(self, script):
        """Executa JavaScript na página."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return None
        try:
            result = self.page.evaluate(script)
            return result
        except Exception as e:
            print(f"❌ Erro ao executar JS: {e}")
            return None

    def get_url(self):
        """Obtém a URL atual."""
        if not self.page:
            print("❌ Erro: Nenhum page disponível.")
            return None
        return self.page.url

    def status(self):
        """Mostra o status do bot."""
        print(f"🤖 {self.name}")
        print(f"   Navegador: {'✅ Inicializado' if self.browser else '❌ Não inicializado'}")
        print(f"   Página: {'✅ Carregada' if self.page else '❌ Nenhuma'}")
        if self.page:
            print(f"   URL: {self.get_url()}")
            print(f"   Título: {self.get_title()}")

    def run_command(self, command_str):
        """Interpreta e executa um comando textual."""
        parts = command_str.strip().split(' ', 2)
        cmd = parts[0].lower()
        
        if cmd == 'open' and len(parts) > 1:
            return self.go_to(parts[1])
        elif cmd == 'click' and len(parts) > 1:
            return self.click(parts[1])
        elif cmd == 'type' and len(parts) > 2:
            return self.type(parts[1], parts[2])
        elif cmd == 'screenshot':
            filename = parts[1] if len(parts) > 1 else "screenshot.png"
            return self.screenshot(filename)
        elif cmd == 'title':
            return self.get_title()
        elif cmd == 'url':
            return self.get_url()
        elif cmd == 'text':
            selector = parts[1] if len(parts) > 1 else None
            return self.get_text(selector)
        elif cmd == 'js' and len(parts) > 1:
            return self.execute_js(parts[1])
        elif cmd == 'status':
            self.status()
            return True
        elif cmd == 'help':
            self.show_help()
            return True
        else:
            print(f"❌ Comando desconhecido: {cmd}")
            return False

    def show_help(self):
        """Mostra ajuda dos comandos."""
        print(f"""
✨ BrowserBot Comandos:

  open <url>           - Abre uma URL
  click <selector>     - Clica em um elemento (ex: #botao)
  type <selector> <txt> - Digita em um campo
  screenshot [arquivo] - Tira captura de tela
  title                - Título da página
  url                  - URL atual
  text [selector]      - Texto da página/elemento
  js <código>          - Executa JavaScript
  status               - Status do bot
  help                 - Esta ajuda
        """)


def main():
    """Modo standalone - roda o bot via linha de comando."""
    bot = BrowserBot("CloudBrowser")
    
    if not bot.initialize():
        sys.exit(1)
    
    print("Digite 'help' para comandos, 'sair' para encerrar.")
    
    while True:
        try:
            cmd = input("\n🌐 browser> ").strip()
            if not cmd:
                continue
            if cmd.lower() in ('sair', 'exit', 'quit'):
                print("Encerrando BrowserBot...")
                break
            bot.run_command(cmd)
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")


if __name__ == "__main__":
    main()