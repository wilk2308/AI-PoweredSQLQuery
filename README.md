# 🧠 AI-Powered SQL Query Assistant

Este projeto é um assistente de consulta SQL inteligente, construído com **LangChain**, **Streamlit**, **OpenAI GPT-3** e **Snowflake**. Ele transforma instruções em linguagem natural em consultas SQL automáticas e executa essas consultas diretamente em um banco de dados **Snowflake**.

---

## 🚀 **Funcionalidades**

- 💬 Gera automaticamente consultas SQL a partir de prompts em linguagem natural usando o modelo GPT-3.
- ❄️ Executa queries diretamente no banco de dados **Snowflake**.
- 📊 Exibe os resultados das consultas em uma interface amigável.
- 🏷️ Armazena prompts e SQLs gerados para treinamento futuro.
- 🗺️ Exibe um **Diagrama de Relacionamento de Entidades (ERD)** para visualização do banco de dados.

---

## 🔧 **Instalação**

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/AI-PoweredSQLQueryAssistant.git
cd AI-PoweredSQLQueryAssistant
```
### 2️⃣ Crie e ative um ambiente virtual:
```bash
python -m venv venv
```
# No Windows
```bash
.\venv\Scripts\activate
```
# No Linux/Mac
```bash
source venv/bin/activate
```
### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

🔑 Configuração da API
Crie um arquivo chamado app_secrets.py e adicione sua chave de API da OpenAI:

OPENAI_API_KEY = "sua-chave-da-openai"
Configure suas credenciais do Snowflake no arquivo sql_execution.py.

💻 Como executar
Inicie a aplicação Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

📋 Como usar
Digite uma pergunta em linguagem natural, como:

```csharp

Quais são as vendas totais do último mês?

O aplicativo:

🔍 Gera a consulta SQL automaticamente usando o modelo GPT-3.
❄️ Executa a consulta no banco de dados Snowflake.
📊 Exibe os resultados diretamente na interface.
Você pode visualizar:

📝 Consulta SQL gerada na aba "Query".
📊 Resultados da execução na aba "Results".
🗺️ Diagrama ER na aba "ER Diagram".
Adicione os prompts gerados ao arquivo de treinamento clicando no botão "Add to training data".
```
🧑‍💻 Estrutura do Projeto
```bash

AI-PoweredSQLQueryAssistant/
│
├── images/                  # Contém o Diagrama ERD
├── prompts/                 # Contém os templates de prompt YAML
├── trainings/               # Armazena dados de treinamento
│
├── app.py                   # Arquivo principal da aplicação
├── app_secrets.py           # Chave da API OpenAI (não subir para o GitHub)
├── sql_execution.py         # Conexão e execução de queries no Snowflake
├── requirements.txt         # Lista de dependências
└── README.md                # Documentação do projeto
```

📦 Dependências Principais
LangChain
Streamlit
OpenAI
Snowflake Connector

🛡️ Contribuição e Licença
Sinta-se à vontade para enviar pull requests ou abrir issues.

Licenciado sob a MIT License.

📫 Contato
Se tiver alguma dúvida ou sugestão, entre em contato:

📧 E-mail: william.sousa@wfitech.com.br
🔗 LinkedIn: https://www.linkedin.com/in/williamsousa-dev