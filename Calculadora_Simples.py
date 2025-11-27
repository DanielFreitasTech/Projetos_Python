def somar(x, y):
    """Realiza adição de dois números."""
    return x + y


def subtrair(x, y):
    """Realiza subtração de dois números."""
    return x - y


def multiplicar(x, y):
    """Realiza multiplicação de dois números."""
    return x * y


def dividir(x, y):
    """Realiza divisão de dois números com validação."""
    if y == 0:
        raise ValueError("Erro! Não é possível dividir por zero.")
    return x / y


def obter_numero(mensagem):
    """Solicita um número válido ao usuário."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Erro: Digite um número válido!")


def obter_nome_usuario():
    """Solicita o nome do usuário."""
    while True:
        nome = input("Por favor, digite seu nome: ").strip()
        if nome:
            return nome
        print("❌ O nome não pode estar vazio. Tente novamente.")


def exibir_menu():
    """Exibe o menu de operações."""
    print("\n" + "=" * 40)
    print("Selecione a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    print("=" * 40)


def processar_operacao(escolha, num1, num2):
    """Processa a operação escolhida e retorna o resultado."""
    try:
        if escolha == '1':
            resultado = somar(num1, num2)
            operacao = "+"
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            operacao = "-"
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            operacao = "*"
        elif escolha == '4':
            resultado = dividir(num1, num2)
            operacao = "/"
        else:
            return None

        print(f"\n✓ Resultado: {num1} {operacao} {num2} = {resultado}")
        return resultado
    except ValueError as e:
        print(f"❌ {e}")
        return None


def main():
    """Função principal da calculadora."""
    print("\n" + "=" * 40)
    print("Bem-vindo à Calculadora Simples!")
    print("=" * 40)
    
    nome = obter_nome_usuario()
    print(f"\n👋 Olá, {nome}! Vamos começar a calcular.\n")

    while True:
        exibir_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5): ").strip()

        if escolha == '5':
            print(f"\n✨ Obrigado por usar a calculadora, {nome}! Até logo.")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")
                processar_operacao(escolha, num1, num2)
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")
        else:
            print("❌ Entrada inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()