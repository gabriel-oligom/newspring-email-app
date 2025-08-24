# Newspring Email App📩
Aplicação automatizada para envio de notícias por e-mail, consumindo dados de **APIs** externas para entregar os principais destaques da semana diretamente na sua caixa de entrada.

## Funcionalidades

- Buscar notícias de uma API pública
- Organizar e formatar as notícias
- Enviar por e-mail automaticamente
- Suporta agendamento automático com **PythonAnywhere**


## 🛠️ Tecnologias Utilizadas
- **Python** – linguagem principal
- **Requests** – para consumir a API de notícias
- **SMTP/SSL** – para envio seguro de e-mails pelo Gmail
- **JSON** – para manipulação dos dados retornados da API
- **REST API** – integração com serviços externos


## 📚 Aprendizados
Desenvolvendo o Newspring Email App eu consegui aprender e praticar:
- Consumo de APIs REST (NewsAPI)
- Estruturação de código em funções e módulos
- Envio seguro de e-mails com SMTP/SSL
- Formatação de relatórios automatizados
- Automação de tarefas e deploy em PythonAnywhere


## ⚙️ Configuração do ambiente
Este projeto usa variáveis de ambiente para proteger suas credenciais de e-mail.  
Siga os passos abaixo para configurar:

1. Crie um arquivo `.env` na raiz do projeto.
2. Copie as variáveis do `.env.example` para o `.env`.
3. Preencha com seus dados:
   - `EMAIL_USER`: seu e-mail Gmail que enviará os e-mails.
   - `EMAIL_PASSWORD`: senha de app gerada pelo Gmail (não use sua senha normal).
   - `EMAIL_RECEIVER`: e-mail que receberá as notícias.
4. **Nunca comite seu `.env` real** no GitHub.


## ⚙️ Automação
O projeto foi configurado para rodar automaticamente usando **PythonAnywhere**, que permite agendar a execução de scripts Python em horários específicos.

O envio de notícias pode ser configurado para rodar de forma 
automática toda semana, sem precisar executar o código manualmente.
 
📌 Para reproduzir:
1. Crie uma conta no [PythonAnywhere](https://www.pythonanywhere.com/)
2. Faça upload do script para a plataforma
3. Configure um "Scheduled Task" no painel, definindo o horário e frequência de execução
4. O PythonAnywhere irá rodar o script e enviar o e-mail automaticamente