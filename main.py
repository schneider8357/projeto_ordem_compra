"""
Registro de ordem de compra - comunicação interdepartamental

- ID
- motivação
- valor
- data aquisição
- data_vencimento
- data_pagamento
- quem (cadastro, cnpj, dados bancarios)
- tem nota fiscal? (bool)

"""

list_usuarios = [
    ("lucas", "12345"),
    ("davi", "12345"),
    ("admin", "admin"),
]

PROMPT_MENU = """#### Registro de ordem de compra ####
Selecione a opção abaixo:
1 - Criar novo Registro
2 - Listar todos os Registros
3 - Obter detalhes de um Registro
4 - Atualizar Registro existente
5 - Remover Registro
6 - Sair do programa
"""

# CRUD
# Create
# Read
# Update
# Delete

dict_registros = dict()

proximo_id = 1

{
    1: {
        "motivacao": "realização de reparo de bomba e bicos injetores da Fiat Strada por solicitação do supervisor de manutenção",
        "valor": 1800.00,
        "data_aquisicao": "01/10/2024",
        "data_vencimento": "12/10/2024",
        "data_pagamento": "10/10/2024",
        "fornecedor": {
            "nome_ou_razao_social": "João do Bico",
            "cpf_ou_cnpj": "000.000.000-01",
            "dados_bancarios": {
                "chave_pix": "abcdefg123456789",
            },
            "telefone": "11 123456678",
            "email": "joaodobico@gmail.com",
        },
        "nota_fiscal": False,
    }
}

def criar_registro(motivacao, valor, data_aquisicao, data_vencimento, fornecedor, nota_fiscal):
    global proximo_id
    dict_registros[proximo_id] = {
        "motivacao": motivacao,
        "valor": valor,
        "data_aquisicao": data_aquisicao,
        "data_vencimento": data_vencimento,
        "data_pagamento": None,
        "fornecedor": fornecedor,
        "nota_fiscal": nota_fiscal,
    }
    proximo_id += 1

def obter_registro():
    ...

def atualizar_registro():
    ...

def remover_registro():
    ...


def menu_principal():
    while True:
        opcao = input(PROMPT_MENU).strip()
        if opcao == "1":
            print("Você selecionou Criar novo Registro")
            motivacao = input("Digite a motivacao do Registro")
            valor = float(input("Digite a valor do Registro"))
            data_aquisicao = input("Digite a data_aquisicao do Registro")
            data_vencimento = input("Digite a data_vencimento do Registro")
            nome_fornecedor = input("Digite nome_ou_razao_social do fornecedor do Registro")
            cpf_ou_cnpj = input("Digite cpf_ou_cnpj do fornecedor do Registro")
            chave_pix = input("Digite chave_pix do fornecedor do Registro")
            telefone = input("Digite telefone do fornecedor do Registro")
            email = input("Digite email do fornecedor do Registro")
            nota_fiscal = input("O Registro possui nota fiscal? (s/n)").strip().lower() in ("s", "sim")
            confere = input(f"""Conferência dos dados:
                {motivacao=}
                {valor=}
                {data_aquisicao=}
                {data_vencimento=}
                {nome_fornecedor=}
                {cpf_ou_cnpj=}
                {chave_pix=}
                {telefone=}
                {email=}
                {nota_fiscal=}
            Os dados conferem? (s/n) """).strip().lower() in ("s", "sim")
            fornecedor = {
                "nome_ou_razao_social": nome_fornecedor,
                "cpf_ou_cnpj": cpf_ou_cnpj,
                "dados_bancarios": {"chave_pix": chave_pix},
                "telefone": telefone,
                "email": email,
            }
            if confere:
                criar_registro(motivacao, valor, data_aquisicao, data_vencimento, fornecedor, nota_fiscal)
                input("Registro criado com sucesso! Pressione enter para voltar ao menu.")
            else:
                input("Operação cancelada, pressione enter para voltar ao menu.")
        elif opcao == "2":
            print(dict_registros)
            input("Pressione enter para voltar ao menu.")
        elif opcao == "6":
            if input("Tem certeza que deseja sair?").strip().lower() in ("s", "sim"):
                break


if __name__ == "__main__":
    # Autenticar usuario com login e senha
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    if (usuario, senha) not in list_usuarios:
        print("Usuario ou senha incorretos!")
        exit(1)
    print("Login bem sucedido!")

    # Menu principal
    menu_principal()



