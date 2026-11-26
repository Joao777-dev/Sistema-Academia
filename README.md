🏋️ Sistema Academia — Vitality Fitness

Sistema de gerenciamento para a academia Vitality Fitness, desenvolvido em Python com banco de dados SQLite. A aplicação roda no terminal e permite cadastrar alunos e professores, matricular alunos em planos e consultar informações da academia.

📑 Sumário
Sobre o projeto
Funcionalidades
Planos disponíveis
Tecnologias
Estrutura do projeto
Banco de dados
Como executar
Como usar
Requisitos do sistema
Roadmap
Informações da academia
Licença
📖 Sobre o projeto

O Sistema Academia foi criado para organizar o dia a dia da Vitality Fitness: cadastro de alunos e professores, controle de matrículas e apresentação dos planos e regras da academia. Todos os dados são persistidos em um banco SQLite local (vitality.db).

✨ Funcionalidades
✅ Cadastro de alunos (nome, data de nascimento, CPF e telefone)
✅ Cadastro de professores (mesmos dados cadastrais)
✅ Matrícula em planos — após cadastrar o aluno, o sistema oferece a escolha entre Bronze, Prata e Ouro
✅ Menu "Saiba mais" com planos, horários, regras de convivência e contatos
✅ Área restrita protegida por senha, com comandos administrativos
✅ Persistência em SQLite com relacionamento entre alunos e matrículas (chave estrangeira)
✅ Tratamento de erros nas operações de cadastro e matrícula
📌 Planos disponíveis
Plano	Valor mensal	Benefícios
🥉 Bronze	R$ 89,90	Musculação, horário livre, área cardio e refil de pré-treino (sem aulas coletivas)
🥈 Prata	R$ 119,90	Tudo do Bronze + Muay Thai, Zumba (2 aulas coletivas/semana) e 1 avaliação física mensal gratuita
🥇 Ouro (VIP)	R$ 149,90	Acesso total e ilimitado + 5 convidados/mês, armário privativo e acompanhamento personalizado
🛠️ Tecnologias
Python 3.10+ (o projeto usa match/case, disponível a partir da versão 3.10)
SQLite 3 (módulo sqlite3 da biblioteca padrão — nenhuma dependência externa)
Git para controle de versão
📂 Estrutura do projeto
Sistema-Academia/
├── .gitattributes             # Configurações de atributos do Git (ex.: fim de linha)
├── .gitignore                 # Arquivos ignorados pelo Git (vitality.db)
├── LICENSE                    # Licença MIT
├── README.md                  # Documentação do projeto
├── requerimentos.md           # Requisitos funcionais (RF01 a RF08)
├── main.py                    # Ponto de entrada: menus e fluxo principal
├── vitality.db                # Banco de dados SQLite (gerado localmente)
│
├── cadastro_usuario/
│   └── cadastro.py            # Coleta e validação dos dados do usuário
│
├── planos_alunos/
│   └── planos.py              # Lógica dos planos Bronze, Prata e Ouro
│
├── vitality_database/
│   ├── schema.py              # Criação das tabelas e inserções no banco
│   └── queries/
│       ├── alunos.py          # Consultas relacionadas aos alunos
│       └── professores.py     # Consultas relacionadas aos professores
│
└── area_restrita/
    └── comandos_admin.py      # Criação de senha, login e menu administrativo

O arquivo vitality.db está listado no .gitignore, ou seja, não vai para o repositório: ele é gerado e atualizado localmente. Os arquivos .gitignore e .gitattributes são ocultos e podem não aparecer em alguns gerenciadores de arquivos.

🗄️ Banco de dados

O banco vitality.db possui três tabelas:

dados_alunos
Coluna	Tipo	Observação
id_aluno	INTEGER	Chave primária, autoincremento
nome_aluno	VARCHAR(30)	Obrigatório
data_nasc	VARCHAR(8)	Formato DDMMAAAA
cpf_aluno	VARCHAR(11)	Somente números
telefone	VARCHAR(11)	Somente números
matriculas_alunos
Coluna	Tipo	Observação
id_matricula	INTEGER	Chave primária, autoincremento
plano_aluno	VARCHAR(10)	BRONZE, PRATA ou OURO
aluno_id	INT	Chave estrangeira → dados_alunos.id_aluno
data_matricula	TEXT	Data/hora da matrícula
dados_professores
Coluna	Tipo	Observação
id_professor	INTEGER	Chave primária, autoincremento
nome_professor	VARCHAR(255)	Obrigatório
data_nasc	VARCHAR(8)	Obrigatório
cpf_professor	VARCHAR(11)	Obrigatório
telefone	VARCHAR(11)	Obrigatório
dados_alunos (1) ───< (N) matriculas_alunos
dados_professores   (tabela independente)
🚀 Como executar
Pré-requisitos
Python 3.10 ou superior
Git (opcional, para clonar o repositório)
Passo a passo
bash
# 1. Clone o repositório
git clone https://github.com/Joao777-dev/Sistema-Academia.git

# 2. Entre na pasta do projeto
cd Sistema-Academia

# 3. Execute o sistema
python main.py

Não há dependências para instalar: o projeto usa apenas a biblioteca padrão do Python. Ajuste a URL do git clone caso o nome do repositório seja diferente.

🖥️ Como usar

Ao iniciar, o sistema exibe o menu principal:

[1] CADASTRAR ALUNO
[2] CADASTRAR PROFESSOR
[3] SAIBA MAIS
[4] AREA RESTRITA
[5] SAIR
Opção	O que faz
1 — Cadastrar aluno	Solicita os dados do aluno, grava no banco e abre o menu de escolha de plano
2 — Cadastrar professor	Solicita os dados e grava o professor no banco
3 — Saiba mais	Exibe planos, horários, regras e contatos da academia
4 — Área restrita	Pede senha e libera o menu administrativo
5 — Sair	Encerra o programa
Escolha do plano

Depois de cadastrar um aluno, o sistema exibe:

[1] PLANO BRONZE
[2] PLANO PRATA
[3] PLANO OURO
[4] VOLTAR

Ao escolher um plano, a matrícula é registrada com a data e hora atuais e o sistema confirma com uma mensagem de sucesso.

📋 Requisitos do sistema

Requisitos funcionais definidos em requerimentos.md e o estado atual de cada um:

Código	Requisito	Status
RF01	Cadastrar aluno	✅ Implementado
RF02	Consultar aluno	🔄 Parcial (área restrita)
RF03	Cadastrar profissional	✅ Implementado
RF04	Cadastrar plano	🔄 Planos fixos no código
RF05	Cadastrar matrícula (associar aluno a plano)	✅ Implementado
RF06	Consultar situação da matrícula (ativa, próxima do vencimento ou vencida)	⏳ Planejado
RF07	Cadastrar exercício	⏳ Planejado
RF08	Consultar histórico, respeitando permissões	⏳ Planejado

Ajuste a coluna Status conforme o andamento real do seu projeto.

🗺️ Roadmap
[ ] Consulta de alunos e professores pelo menu
[ ] Cálculo e exibição da situação da matrícula (ativa / próxima do vencimento / vencida)
[ ] Cadastro de exercícios e montagem de fichas de treino
[ ] Histórico de matrículas e treinos por aluno
[ ] Níveis de permissão por tipo de usuário
[ ] Validação de CPF e telefone
[ ] Armazenar senhas da área restrita com hash
[ ] Testes automatizados
[ ] Interface gráfica ou web
📞 Informações da academia
⏰ Horário de funcionamento
Segunda a sexta: 06:00 às 22:00
Sábados e feriados: 08:00 às 14:00
📋 Regras de convivência
Uso obrigatório de toalha de treino
Guardar os pesos e anilhas após o uso
Respeitar as orientações dos professores
📬 Dúvidas e suporte
Recepção: (11) 4002-8922
E-mail: contato@vitalityfitness.com
🤝 Contribuindo

Contribuições são bem-vindas!

Faça um fork do projeto
Crie uma branch para a sua funcionalidade (git checkout -b feature/minha-feature)
Faça o commit (git commit -m "Adiciona minha feature")
Envie para a branch (git push origin feature/minha-feature)
Abra um Pull Request
📄 Licença

Distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Joao777-dev 💪
