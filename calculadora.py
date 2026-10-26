"""
Calculadora em Python - Atividade prática de Coding

Executa adição, subtração, multiplicação e divisão no terminal,
com menu numerado, tratamento de divisão por zero e validação de entradas.
"""

# Códigos de cor ANSI (destaques no terminal)
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"

LINHA_DUPLA = "=" * 42
LINHA_SIMPLES = "-" * 42


# ---------- Operações matemáticas ----------
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None  # sinaliza divisão por zero
    return a / b


# ---------- Funções de apresentação ----------
def exibir_menu():
    print()
    print(LINHA_DUPLA)
    print(f"{AMARELO}{'CALCULADORA EM PYTHON':^42}{RESET}")
    print(LINHA_DUPLA)
    print("  1 - Adição")
    print("  2 - Subtração")
    print("  3 - Multiplicação")
    print("  4 - Divisão")
    print("  0 - Sair")
    print()


def formatar(numero):
    """Mostra números inteiros sem '.0' (ex.: 20.0 -> 20)."""
    if numero == int(numero):
        return str(int(numero))
    return str(round(numero, 10))


# ---------- Funções de entrada ----------
def ler_numero(mensagem):
    """Pede um número até o usuário digitar um valor válido."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print(f"{VERMELHO}Entrada inválida. Digite apenas números.{RESET}")


def ler_opcao():
    """Pede a opção do menu até o usuário digitar uma opção válida."""
    while True:
        opcao = input("Escolha uma opção: ").strip()
        if opcao in ("0", "1", "2", "3", "4"):
            return opcao
        print(f"{VERMELHO}Opção inválida. Escolha entre 0 e 4.{RESET}")


def perguntar_outro_calculo():
    """Pergunta se o usuário deseja fazer outro cálculo (s/n)."""
    while True:
        resposta = input("\nOutro cálculo? (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print(f"{VERMELHO}Responda com 's' para sim ou 'n' para não.{RESET}")


# ---------- Programa principal ----------
def main():
    operacoes = {
        "1": ("+", somar),
        "2": ("-", subtrair),
        "3": ("x", multiplicar),
        "4": ("/", dividir),
    }

    continuar = True
    while continuar:
        exibir_menu()
        opcao = ler_opcao()

        if opcao == "0":
            break

        primeiro_numero = ler_numero("Primeiro número: ")
        segundo_numero = ler_numero("Segundo número: ")

        simbolo, funcao = operacoes[opcao]
        resultado = funcao(primeiro_numero, segundo_numero)

        print()
        if resultado is None:
            print(f"{VERMELHO}Erro: divisão por zero não é permitida.{RESET}")
        else:
            print(
                f"{VERDE}Resultado: {formatar(primeiro_numero)} {simbolo} "
                f"{formatar(segundo_numero)} = {formatar(resultado)}{RESET}"
            )

        continuar = perguntar_outro_calculo()
        if continuar:
            print(f"\n{LINHA_SIMPLES[:10]} MENU PRINCIPAL {LINHA_SIMPLES[:10]}")

    print(f"\n{VERDE}Programa encerrado.{RESET}")


if __name__ == "__main__":
    main()
