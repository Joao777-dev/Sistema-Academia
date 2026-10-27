from validacao_usuario.validacao import (
    validar_cpf,
    validar_nasc,
     validar_tel
)
def cadastro_usuario():
    nome_usuario = input('NOME COMPLETO: ')
    while not nome_usuario: 
        nome_usuario = input('NOME COMPLETO: ').upper()

    while True:
        data_nasc = input('DATA DE NASCIMENTO (DDMMAAAA): ')
        if validar_nasc(data_nasc):
            print('DATA DE NASCIMENTO CADASTRADA COM SUCESSO!')
            break
        else:
            print('DATA DE NASCIMENTO INVALIDA OU INCORETA!')

    while True:
        cpf_usuario = input('CPF: ')
        if validar_cpf(cpf_usuario):
            print('CPF CADASTRADO COM SUCESSO!')
            break
        else:
            print('CPF INVALIDO OU INCORRETO')
    while True:
        tel_usuario = input('TEL: +55')
        if validar_tel(tel_usuario):
            print('TELEFONE CADASTRADO COM SUCESSO!')
            break
        else:
            print(f'NUMERO INVALIDO OU INCORRETO {tel_usuario}')


    return nome_usuario, data_nasc, cpf_usuario, tel_usuario
