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

## ⚙️ Automação
Este projeto foi configurado para rodar automaticamente usando **PythonAnywhere**, que permite agendar a execução de scripts Python em horários específicos.

O envio de notícias pode ser configurado para rodar de forma 
automática toda semana, sem precisar executar o código manualmente.
 
📌 Para reproduzir:
1. Crie uma conta no [PythonAnywhere](https://www.pythonanywhere.com/)
2. Faça upload do script para a plataforma
3. Configure um "Scheduled Task" no painel, definindo o horário e frequência de execução
4. O PythonAnywhere irá rodar o script e enviar o e-mail automaticamente