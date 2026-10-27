from cadastro_usuario.cadastro import (
    cadastro_usuario
)
from planos_alunos.planos import (
    plano_bronze,
    plano_prata,
    plano_ouro
)
from vitality_database.sql_querys import (
    inserir_alunos,
    inserir_matriculas,
    inserir_professores,
)

from datetime import (
    datetime
)

from area_restrita.comandos_admin import(
    menu_admin
)

senha_vitality = 'vitality123'


def menu_cadastro():
    while True:
        print(''' 
[1] CADASTRAR ALUNO
[2] CADASTRAR PROFESSOR
[3] SAIBA MAIS
[4] AREA RESTRITA
[5] SAIR
''')
        opcao_menu = input('OPÇÃO: ').strip()

        match opcao_menu:
            case '1':
                try:
                    nome_usuario, data_nasc, cpf_usuario, tel_usuario = cadastro_usuario()
                    id_usuario = inserir_alunos(nome_usuario, data_nasc, cpf_usuario, tel_usuario)
                    return id_usuario
                except Exception as e:
                    print(f"\n[ERRO] Não foi possível cadastrar o aluno: {e}")
            case '2':
                try:
                    nome_usuario, data_nasc, cpf_usuario, tel_usuario = cadastro_usuario()
                    id_usuario = inserir_professores(nome_usuario, data_nasc, cpf_usuario, tel_usuario)
                    print('\n[SUCESSO] PROFESSOR CADASTRADO COM SUCESSO!')
                except Exception as e:
                    print(f"\n[ERRO] Não foi possível cadastrar o professor: {e}")
            case '3':
                print('''
    ===================================================
                  SAIBA MAIS - VITALITY FITNESS
    ===================================================

    📌 NOSSOS PLANOS:

    [ BRONZE ] - R$ 89,90/mês
    
Acesso à área de musculação
Horário livre
Refil de Pré Treino
Área Cardio
Sem direito a aulas coletivas

    [ PRATA ] - R$ 119,90/mês
    
Musculação + Refil de Pré Treino + Área Cardio  + Muay Thai + Zumba
Direito a 2 aulas coletivas por semana
1 Avaliação física mensal gratuita

    [ OURO ] - R$ 149,90/mês (VIP)
    
Acesso total e ilimitado (Musculação + Aulas + Muay Thai + Zumba)
Direito a trazer 5 convidados mensais
Armário privativo e acompanhamento personalizado

---------------------------------------------------
    ⏰ HORÁRIO DE FUNCIONAMENTO:
    
Segunda a Sexta: 06:00 às 22:00
Sábados e Feriados: 08:00 às 14:00

---------------------------------------------------
    📋 REGRAS DE CONVIVÊNCIA:
    
Uso obrigatório de toalha de treino.
Guarde os pesos e anilhas após o uso.
Respeite as orientações dos professores.

---------------------------------------------------
    📞 DÚVIDAS E SUPORTE:
    
Recepção: (11) 4002-8922
E-mail: contato@vitalityfitness.com''')           
            
            case '4':
                senha_digitada = input('SENHA: ').strip()
                if senha_digitada == senha_vitality:
                    menu_admin()
            case '5':
                print('FINALIZANDO...')
                break

def plano_escolhido(id_usuario):
        while True:
            print('''
        [1] PLANO BRONZE
        [2] PLANO PRATA
        [3] PLANO OURO
        [4] VOLTAR
        ''')
            opcao_plano = input('OPÇÃO: ').strip()
            match opcao_plano:
                case '1':
                    try:
                        plano_bronze()
                        inserir_matriculas("BRONZE", id_usuario, datetime.now())
                        print("\n[SUCESSO] Matrícula realizada no Plano Bronze!")
                        break
                    except Exception as e:
                        print(f"\n[ERRO] Erro ao registrar matrícula: {e}")
                case '2':
                    try:
                        plano_prata()
                        inserir_matriculas("PRATA", id_usuario, datetime.now())
                        print("\n[SUCESSO] Matrícula realizada no Plano Prata!")
                        break
                    except Exception as e:
                        print(f"\n[ERRO] Erro ao registrar matrícula: {e}")
                case '3':
                    try:
                        plano_ouro()
                        inserir_matriculas("OURO", id_usuario, datetime.now())
                        print("\n[SUCESSO] Matrícula realizada no Plano Ouro!")
                        break
                    except Exception as e:
                        print(f"\n[ERRO] Erro ao registrar matrícula: {e}")
                case '4':
                    id_usuario = menu_cadastro()

id_usuario = menu_cadastro()
if id_usuario:
    plano_escolhido(id_usuario)