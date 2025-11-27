# 🧮 Calculadora

Uma calculadora simples, funcional e com interface gráfica, desenvolvida em Python com suporte tanto para uso em terminal quanto em interface visual.

## 📋 Conteúdo

- [Características](#características)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Versões Disponíveis](#versões-disponíveis)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Recursos](#recursos)
- [Tratamento de Erros](#tratamento-de-erros)
- [Exemplos de Uso](#exemplos-de-uso)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## ✨ Características

### Calculadora GUI
- 🖥️ **Interface Gráfica Amigável**: Interface visual intuitiva e responsiva
- 👤 **Personalização**: Saudação personalizada com o nome do usuário
- 📱 **Layout Moderno**: Design profissional com cores bem definidas
- 📊 **Histórico de Cálculos**: Acompanhe todos os cálculos realizados
- ⌨️ **Entrada Flexível**: Suporte a números, operadores e ponto decimal
- 🔒 **Validação Robusta**: Tratamento completo de erros e exceções

### Calculadora em Terminal
- 💻 **Interface CLI**: Versão em linha de comando simples e clara
- 🔄 **Menu Interativo**: Menu de operações fácil de usar
- ✅ **Validação de Entrada**: Verifica números válidos continuamente
- 🛡️ **Tratamento de Erros**: Mensagens claras em caso de erros

## 📦 Pré-requisitos

- **Python 3.6+** instalado no seu computador
- Nenhuma dependência externa necessária (usa apenas biblioteca padrão do Python)

### Verificar versão do Python

```bash
python --version
```

## 🚀 Instalação

1. **Clone ou baixe o repositório:**
```bash
git clone <seu-repositorio>
cd Calculadora
```

2. **Verifique se o Python está instalado:**
```bash
python --version
```

3. **Pronto!** Não há dependências para instalar.

## 📖 Como Usar

### Versão com Interface Gráfica (Recomendado)

Execute o arquivo principal:

```bash
python Calculadora_GUI.py
```

**Passos:**
1. A janela de boas-vindas aparecerá
2. Digite seu nome no campo de entrada
3. Clique em "Continuar" ou pressione Enter
4. Use os botões para realizar cálculos
5. Clique em "=" para obter o resultado

**Botões Disponíveis:**
- **Números (0-9)**: Adiciona dígitos à expressão
- **Operadores (+, -, ×, ÷)**: Realiza operações matemáticas
- **Ponto (.)**: Adiciona números decimais
- **= (Igual)**: Calcula e exibe o resultado
- **C (Limpar)**: Limpa o display
- **📋 Histórico**: Mostra todos os cálculos anteriores
- **Sair**: Encerra a aplicação

### Versão em Terminal

Execute o arquivo alternativo:

```bash
python Calculadora_Simples.py
```

**Passos:**
1. Forneça seu nome quando solicitado
2. Selecione a operação (1-5)
3. Digite os dois números
4. Visualize o resultado
5. Repita ou pressione 5 para sair

## 📁 Versões Disponíveis

### Calculadora_GUI.py
- **Versão com Interface Gráfica**
- Ideal para uso diário
- Layout visual profissional
- Histórico de cálculos
- Melhor experiência do usuário

### Calculadora_Simples.py
- **Versão em Terminal/CLI**
- Simples e direta
- Sem dependências de interface gráfica
- Perfeita para automação ou scripts
- Validação robusta de entrada

## 🗂️ Estrutura do Projeto

```
Calculadora/
├── Calculadora_GUI.py          # Versão com Interface Gráfica (tkinter)
├── Calculadora_Simples.py      # Versão em Terminal (CLI)
└── README.md                    # Este arquivo
```

## 🎯 Recursos

### Operações Matemáticas Suportadas

| Operação | Símbolo | Exemplo |
|----------|---------|---------|
| Adição | + | 5 + 3 = 8 |
| Subtração | - | 10 - 4 = 6 |
| Multiplicação | × ou * | 6 × 7 = 42 |
| Divisão | ÷ ou / | 15 ÷ 3 = 5 |

### Funcionalidades Especiais

- ✅ Suporte a números decimais
- ✅ Histórico de até 50 cálculos
- ✅ Saudação personalizada
- ✅ Validação de entrada
- ✅ Tratamento de divisão por zero
- ✅ Interface responsiva

## 🛡️ Tratamento de Erros

A calculadora trata os seguintes erros automaticamente:

### GUI
- **Entrada Vazia**: Pede nome válido na tela inicial
- **Expressão Inválida**: Mostra mensagem de erro clara
- **Divisão por Zero**: Alerta específico do erro
- **Caracteres Inválidos**: Ignora automaticamente

### Terminal
- **Número Inválido**: Solicita novamente até receber entrada válida
- **Nome Vazio**: Não permite prosseguir sem nome
- **Divisão por Zero**: Exibe mensagem de erro
- **Entrada Inválida**: Pede nova tentativa

## 💡 Exemplos de Uso

### Exemplo 1: Operação Simples
```
Nome: João
Operação: Somar
Primeiro número: 10
Segundo número: 5
Resultado: 10 + 5 = 15
```

### Exemplo 2: Divisão
```
Nome: Maria
Operação: Dividir
Primeiro número: 100
Segundo número: 4
Resultado: 100 / 4 = 25.0
```

### Exemplo 3: Cálculo com Decimais (GUI)
```
Expressão: 2.5 × 4
Resultado: 10.0
```

## 🔧 Desenvolvimento

### Estrutura do Código (GUI)

A aplicação segue o padrão Orientado a Objetos:

- **Classe `Calculadora`**: Contém as operações matemáticas
  - `somar(x, y)`: Soma dois números
  - `subtrair(x, y)`: Subtrai dois números
  - `multiplicar(x, y)`: Multiplica dois números
  - `dividir(x, y)`: Divide dois números com validação

- **Classe `CalculadoraGUI`**: Gerencia a interface
  - `criar_tela_inicio()`: Interface de boas-vindas
  - `criar_tela_calculadora()`: Interface principal
  - `calcular()`: Processa expressão matemática
  - `mostrar_historico()`: Exibe histórico de cálculos

### Melhorias Implementadas

- ✅ Tratamento completo de exceções
- ✅ Validação robusta de entrada
- ✅ Código bem documentado
- ✅ Interface responsiva e intuitiva
- ✅ Histórico persistente na sessão
- ✅ Formatação de números flutuantes
- ✅ Bloqueio de operações inválidas

## 📝 Exemplos de Código

### Usando as funções da calculadora

```python
from Calculadora_GUI import Calculadora

calc = Calculadora()

# Soma
resultado = calc.somar(10, 5)  # 15

# Divisão com validação
try:
    resultado = calc.dividir(10, 2)  # 5.0
except ValueError as e:
    print(f"Erro: {e}")
```

## 🐛 Resolução de Problemas

### A interface gráfica não abre

**Solução 1**: Verifique se o tkinter está instalado
```bash
python -c "import tkinter; print('tkinter está instalado')"
```

**Solução 2**: Reinstale o tkinter
```bash
# Windows
python -m pip install tk

# Linux
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

### Erros ao executar o script

**Problema**: `ModuleNotFoundError: No module named 'tkinter'`
```bash
# Instale tkinter
python -m pip install tk
```

**Problema**: Permissão negada
```bash
# Conceda permissão de execução (Linux/Mac)
chmod +x Calculadora_GUI.py
```

## 📚 Documentação Adicional

### Métodos da Classe CalculadoraGUI

| Método | Descrição |
|--------|-----------|
| `criar_tela_inicio()` | Cria interface de boas-vindas |
| `criar_tela_calculadora()` | Cria interface principal da calculadora |
| `calcular()` | Avalia expressão e exibe resultado |
| `limpar()` | Limpa o display |
| `mostrar_historico()` | Abre janela com histórico de cálculos |
| `sair()` | Encerra a aplicação |

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como uma calculadora educacional e funcional em Python.

## 📞 Suporte

Se encontrar problemas ou tiver sugestões, por favor:
- Abra uma Issue no repositório
- Entre em contato através do email
- Verifique o arquivo de Resolução de Problemas acima

## 🎓 Conceitos Aprendidos

Este projeto demonstra:
- Programação Orientada a Objetos em Python
- Interface gráfica com tkinter
- Tratamento de exceções
- Validação de entrada
- Estrutura de projetos Python
- Boas práticas de código

## 🚀 Roadmap Futuro

- [ ] Modo científico com mais operações
- [ ] Temas personalizáveis
- [ ] Exportar histórico para arquivo
- [ ] Cálculos em diferentes bases numéricas
- [ ] Interface responsiva para mobile
- [ ] Testes unitários automatizados
- [ ] Versão web

---

**Obrigado por usar a Calculadora!** 🎉

Última atualização: 26 de novembro de 2025
