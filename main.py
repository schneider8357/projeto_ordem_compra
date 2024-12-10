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
import json


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
4 - Remover Registro
5 - Atualizar Registro existente
6 - Salvar base de dados
7 - Importar base de dados
8 - Sair do programa
"""

ARQUIVO_BASE_JSON = "base_registros.json"

# CRUD
# Create
# Read
# Update
# Delete

dict_registros = dict()


"""
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
    },
    2: {

    },
    3: {

    },
    4: {

    },
}
"""
def confirma(msg):
    return input(msg).strip().lower() in ("s", "sim")

def criar_registro(motivacao, valor, data_aquisicao, data_vencimento, fornecedor, nota_fiscal):
    proximo_id = (max(dict_registros.keys()) + 1) if dict_registros else 1
    dict_registros[proximo_id] = {
        "id": proximo_id,
        "motivacao": motivacao,
        "valor": valor,
        "data_aquisicao": data_aquisicao,
        "data_vencimento": data_vencimento,
        "data_pagamento": None,
        "fornecedor": fornecedor,
        "nota_fiscal": nota_fiscal,
    }

def obter_registros(id_registro):
    return [
        dict_registros[id_registro],
    ]

def remover_registro(id_registro):
    dict_registros.pop(int(id_registro))

def atualizar_registro():
    ...

def salvar_base_json(nome_arquivo):
    dados_json = json.dumps(dict_registros)
    with open(nome_arquivo, "w") as f:
        f.write(dados_json)

def carregar_base_json(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        dict_registros.clear()
        dict_registros.update(json.loads(f.read()))

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
            nota_fiscal = confirma("O Registro possui nota fiscal? (s/n)")
            confere = confirma(f"""Conferência dos dados:
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
            Os dados conferem? (s/n) """)
            fornecedor = {
                "nome_ou_razao_social": nome_fornecedor,
                "cpf_ou_cnpj": cpf_ou_cnpj,
                "dados_bancarios": {"chave_pix": chave_pix},
                "telefone": telefone,
                "email": email,
            }
            if confere:
                criar_registro(motivacao, valor, data_aquisicao, data_vencimento, fornecedor, nota_fiscal)
                print("Registro criado com sucesso!")
            else:
                print("Operação cancelada")
        elif opcao == "2":
            for k,v in dict_registros.items():
                print(k, v)
        elif opcao == "3":
            id_registro = input("Digite o ID do Registro que deseja consultar: ")
            if not id_registro.isnumeric():
                input("Operação cancelada, digite um ID numérico (int).\nPressione enter para continuar.")
                continue
            list_registros = obter_registros(int(id_registro))
            print(f"Foram encontrados {len(list_registros)} Registros")
            for reg in list_registros:
                print(f"""Registro ID {reg["id"]}:
                    {reg["motivacao"]=}
                    {reg["valor"]=}
                    {reg["data_aquisicao"]=}
                    {reg["data_vencimento"]=}
                    {reg["data_pagamento"]=}
                    {reg["fornecedor"]["nome_ou_razao_social"]=}
                    {reg["fornecedor"]["cpf_ou_cnpj"]=}
                    {reg["fornecedor"]["dados_bancarios"]["chave_pix"]=}
                    {reg["fornecedor"]["telefone"]=}
                    {reg["fornecedor"]["email"]=}
                    {reg["nota_fiscal"]=}""")
        elif opcao == "4":
            id_registro = input("Digite o ID do Registro que deseja remover: ")
            registros = obter_registros(int(id_registro))
            if not registros:
                print(f"Não foi encontrado registro com o ID {id_registro}.")
                continue
            remover_registro(int(id_registro))
        elif opcao == "5":
            print("Ainda não implementado")
        elif opcao == "6":
            nome_arquivo = input(f"Digite o nome do arquivo para salvar a base ou pressione enter para utilizar valor padrão ({ARQUIVO_BASE_JSON})") or ARQUIVO_BASE_JSON
            salvar_base_json(nome_arquivo)
            print("Base salva com sucesso!")
        elif opcao == "7":
            nome_arquivo = input(f"Digite o nome do arquivo para carregar a base ou pressione enter para utilizar valor padrão ({ARQUIVO_BASE_JSON})") or ARQUIVO_BASE_JSON
            if confirma("Tem certeza que deseja carregar a base? Isso irá sobrescrever as alterações atuais! (s/n)"):
                carregar_base_json(nome_arquivo)
                print("Base carregada com sucesso!")
            else:
                print("Operação cancelada")
        elif opcao == "8":
            if input("Tem certeza que deseja sair?").strip().lower() in ("s", "sim"):
                break
        input("Pressione enter para voltar ao menu.")

def login():
    usuario = input("Digite o seu login: ")
    senha = input("Digite a sua senha: ")
    if (usuario, senha) not in list_usuarios:
        return False
    return True


if __name__ == "__main__":
    # Autenticar usuario com login e senha
    if login():
        # Menu principal
        print("Login bem sucedido!")
        menu_principal()
    else:
        print("Usuario ou senha incorretos!")
    

