# Funções com argumentos padrão e *args, **kwargs
def saudacao(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

saudacao("Vitor")
saudacao("San", "Bom dia")

# Função com *args e **kwargs
def exemplo_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

exemplo_args_kwargs(1, 2, 3, nome="Vitor", idade=20)

# Decorador de função
def meu_decorador(funcao):
    def wrapper():
        print("Executando algo antes da função")
        funcao()
        print("Executando algo depois da função")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função executada!")

minha_funcao()
