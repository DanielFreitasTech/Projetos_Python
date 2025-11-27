import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont


class Calculadora:
    """Classe que implementa as operações matemáticas básicas."""
    
    @staticmethod
    def somar(x, y):
        """Realiza adição de dois números."""
        return x + y

    @staticmethod
    def subtrair(x, y):
        """Realiza subtração de dois números."""
        return x - y

    @staticmethod
    def multiplicar(x, y):
        """Realiza multiplicação de dois números."""
        return x * y

    @staticmethod
    def dividir(x, y):
        """Realiza divisão de dois números com validação."""
        if y == 0:
            raise ValueError("Erro! Não é possível dividir por zero.")
        return x / y


class CalculadoraGUI:
    """Interface gráfica para a calculadora."""
    
    def __init__(self, root):
        """Inicializa a aplicação da calculadora."""
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Configurar estilo
        self.root.configure(bg="#f0f0f0")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Cores
        self.cor_fundo = "#f0f0f0"
        self.cor_display = "#2c3e50"
        self.cor_botao = "#3498db"
        self.cor_botao_operacao = "#e74c3c"
        self.cor_botao_igual = "#27ae60"
        
        # Variáveis
        self.entrada_display = tk.StringVar(value="0")
        self.nome_usuario = ""
        self.historico = []
        
        # Construir interface
        self.criar_tela_inicio()
    
    def criar_tela_inicio(self):
        """Cria a tela de boas-vindas com entrada do nome."""
        # Limpar janela
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        frame_principal = ttk.Frame(self.root, padding="20")
        frame_principal.pack(expand=True, fill="both")
        
        # Título
        titulo = ttk.Label(
            frame_principal,
            text="Bem-vindo à Calculadora!",
            font=("Helvetica", 20, "bold")
        )
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = ttk.Label(
            frame_principal,
            text="Qual é o seu nome?",
            font=("Helvetica", 12)
        )
        subtitulo.pack(pady=10)
        
        # Campo de entrada de nome
        self.entrada_nome = ttk.Entry(
            frame_principal,
            font=("Helvetica", 12),
            width=30
        )
        self.entrada_nome.pack(pady=10, ipady=8)
        self.entrada_nome.focus()
        
        # Botão para continuar
        botao_continuar = ttk.Button(
            frame_principal,
            text="Continuar",
            command=self.validar_nome
        )
        botao_continuar.pack(pady=20, fill="x", ipady=10)
        
        # Permitir Enter para continuar
        self.entrada_nome.bind("<Return>", lambda e: self.validar_nome())
    
    def validar_nome(self):
        """Valida o nome do usuário."""
        nome = self.entrada_nome.get().strip()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, digite seu nome!")
            self.entrada_nome.focus()
            return
        
        self.nome_usuario = nome
        self.criar_tela_calculadora()
    
    def criar_tela_calculadora(self):
        """Cria a interface principal da calculadora."""
        # Limpar janela
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        frame_principal = tk.Frame(self.root, bg=self.cor_fundo)
        frame_principal.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Saudação
        saudacao = tk.Label(
            frame_principal,
            text=f"Olá, {self.nome_usuario}!",
            font=("Helvetica", 12, "bold"),
            bg=self.cor_fundo
        )
        saudacao.pack(pady=10)
        
        # Display da calculadora
        self.display = tk.Label(
            frame_principal,
            textvariable=self.entrada_display,
            font=("Helvetica", 24, "bold"),
            bg=self.cor_display,
            fg="white",
            padx=20,
            pady=20,
            relief="sunken",
            bd=2,
            anchor="e",
            justify="right"
        )
        self.display.pack(fill="x", pady=10)
        
        # Frame para botões
        frame_botoes = tk.Frame(frame_principal, bg=self.cor_fundo)
        frame_botoes.pack(fill="both", expand=True, pady=10)
        
        # Layout dos botões
        botoes_layout = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]
        
        for linha in botoes_layout:
            frame_linha = tk.Frame(frame_botoes, bg=self.cor_fundo)
            frame_linha.pack(fill="both", expand=True, padx=5, pady=5)
            
            for botao_texto in linha:
                self.criar_botao(frame_linha, botao_texto)
        
        # Frame para botões de controle
        frame_controle = tk.Frame(frame_principal, bg=self.cor_fundo)
        frame_controle.pack(fill="x", pady=10)
        
        # Botão Limpar
        botao_limpar = tk.Button(
            frame_controle,
            text="C (Limpar)",
            font=("Helvetica", 10, "bold"),
            bg="#95a5a6",
            fg="white",
            relief="raised",
            bd=2,
            padx=10,
            pady=8,
            command=self.limpar
        )
        botao_limpar.pack(side="left", fill="both", expand=True, padx=2)
        
        # Botão Histórico
        botao_historico = tk.Button(
            frame_controle,
            text="📋 Histórico",
            font=("Helvetica", 10, "bold"),
            bg="#9b59b6",
            fg="white",
            relief="raised",
            bd=2,
            padx=10,
            pady=8,
            command=self.mostrar_historico
        )
        botao_historico.pack(side="left", fill="both", expand=True, padx=2)
        
        # Botão Sair
        botao_sair = tk.Button(
            frame_controle,
            text="Sair",
            font=("Helvetica", 10, "bold"),
            bg="#c0392b",
            fg="white",
            relief="raised",
            bd=2,
            padx=10,
            pady=8,
            command=self.sair
        )
        botao_sair.pack(side="left", fill="both", expand=True, padx=2)
    
    def criar_botao(self, frame, texto):
        """Cria um botão da calculadora."""
        # Definir cores baseadas no tipo de botão
        if texto in ["÷", "×", "-", "+"]:
            bg = self.cor_botao_operacao
        elif texto == "=":
            bg = self.cor_botao_igual
        else:
            bg = self.cor_botao
        
        botao = tk.Button(
            frame,
            text=texto,
            font=("Helvetica", 14, "bold"),
            bg=bg,
            fg="white",
            relief="raised",
            bd=2,
            command=lambda: self.ao_clicar_botao(texto),
            activebackground=bg,
            activeforeground="white"
        )
        botao.pack(side="left", fill="both", expand=True, padx=2)
    
    def ao_clicar_botao(self, texto):
        """Processa o clique em um botão."""
        if texto == "=":
            self.calcular()
        elif texto == "÷":
            self.adicionar_operador(" / ")
        elif texto == "×":
            self.adicionar_operador(" * ")
        elif texto == "-":
            self.adicionar_operador(" - ")
        elif texto == "+":
            self.adicionar_operador(" + ")
        else:
            self.adicionar_numero(texto)
    
    def adicionar_numero(self, numero):
        """Adiciona um número ao display."""
        display_atual = self.entrada_display.get()
        
        if display_atual == "0" and numero != ".":
            self.entrada_display.set(numero)
        elif numero == "." and "." in display_atual:
            return
        else:
            self.entrada_display.set(display_atual + numero)
    
    def adicionar_operador(self, operador):
        """Adiciona um operador ao display."""
        display_atual = self.entrada_display.get().strip()
        
        if display_atual and not display_atual.endswith(" "):
            self.entrada_display.set(display_atual + operador)
    
    def calcular(self):
        """Calcula o resultado da expressão."""
        try:
            expressao = self.entrada_display.get().strip()
            
            # Validar expressão
            if not expressao or expressao.endswith(" "):
                messagebox.showerror("Erro", "Expressão inválida!")
                return
            
            # Avaliar a expressão
            resultado = eval(expressao)
            
            # Adicionar ao histórico
            self.historico.append(f"{expressao} = {resultado}")
            
            # Limitar histórico a 50 itens
            if len(self.historico) > 50:
                self.historico.pop(0)
            
            # Formatar resultado
            if isinstance(resultado, float):
                if resultado == int(resultado):
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 10)
            
            self.entrada_display.set(str(resultado))
            
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Não é possível dividir por zero!")
            self.entrada_display.set("0")
        except Exception as e:
            messagebox.showerror("Erro", f"Expressão inválida!\n{str(e)}")
            self.entrada_display.set("0")
    
    def limpar(self):
        """Limpa o display."""
        self.entrada_display.set("0")
    
    def mostrar_historico(self):
        """Mostra o histórico de cálculos."""
        if not self.historico:
            messagebox.showinfo("Histórico", "Nenhum cálculo realizado ainda!")
            return
        
        # Criar janela de histórico
        janela_historico = tk.Toplevel(self.root)
        janela_historico.title("Histórico de Cálculos")
        janela_historico.geometry("400x300")
        janela_historico.configure(bg=self.cor_fundo)
        
        # Frame com scrollbar
        frame_scroll = ttk.Frame(janela_historico)
        frame_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(frame_scroll)
        scrollbar.pack(side="right", fill="y")
        
        listbox = tk.Listbox(
            frame_scroll,
            font=("Helvetica", 10),
            yscrollcommand=scrollbar.set,
            bg="white",
            fg=self.cor_display
        )
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)
        
        # Adicionar itens do histórico
        for i, calculo in enumerate(self.historico, 1):
            listbox.insert(tk.END, f"{i}. {calculo}")
        
        # Botão para limpar histórico
        botao_limpar = ttk.Button(
            janela_historico,
            text="Limpar Histórico",
            command=self.limpar_historico
        )
        botao_limpar.pack(fill="x", padx=10, pady=5)
    
    def limpar_historico(self):
        """Limpa o histórico de cálculos."""
        self.historico.clear()
        messagebox.showinfo("Sucesso", "Histórico limpo!")
    
    def sair(self):
        """Encerra a aplicação."""
        if messagebox.askyesno("Sair", f"Obrigado por usar a calculadora, {self.nome_usuario}! Deseja sair?"):
            self.root.quit()


def main():
    """Função principal."""
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
