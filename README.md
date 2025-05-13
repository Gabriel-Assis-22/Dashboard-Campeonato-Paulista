# 📊 Dashboard Campeonato Paulista

Este projeto é um dashboard interativo desenvolvido com **Python**, **Streamlit** e **Plotly**, para análise histórica dos times participantes do Campeonato Paulista de Futebol.

## 📌 Descrição

O objetivo do projeto é proporcionar uma visualização dinâmica e personalizável de informações históricas do Campeonato Paulista, permitindo ao usuário filtrar dados por time, divisões e estatísticas como gols, pontos, participações e aproveitamento.

## 🚀 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

## 📥 Como Executar

1. **Clone o repositório:**
git clone https://github.com/seu-usuario/Dashboard-Campeonato-Paulista.git

2. **Acesse o diretório do projeto:**
cd Dashboard-Campeonato-Paulista

4. **Crie e ative seu ambiente virtual:**
python -m venv venv
venv\Scripts\activate   # no Windows
source venv/bin/activate  # no Linux/Mac

5. **Instale as dependências:**
pip install -r requirements.txt

6. **Se ainda não tiver o arquivo requirements.txt, você pode criar com:**
pip freeze > requirements.txt

7. **Execute o aplicativo:**
streamlit run app.py

📊 **Funcionalidades**

- Filtro por times

- Filtro por quantidade de participações

- Filtro por divisões (Série A, A2, A3 e B)

**Resumo geral de:**

- Total de Pontos

- Total de Partidas

- Total de Gols

**Gráficos:**

📈 Gols por Clube

📈 Pontos por Clube

📈 Participações por Clube

📈 Aproveitamento por Clube

📊 Distribuição de Gols

🏆 Clube com Mais Gols

🏆 Clube com Mais Participações

🏆 Clube com Melhor Saldo de Gols

📊 Taxa de Vitórias

📊 Exemplo de Visualização

👨‍💻 Desenvolvido por:
Cleiton Rodrigues | Douglas Mariano | Gabriel Roberto | Lysis Relvas

📌 Observações
**Certifique-se de alterar o caminho do arquivo CSV no código (caminho_arquivo) para o diretório correto no seu ambiente:**
caminho_arquivo = "C:\seu-caminho\campeonato_paulista_ranking_historico.csv"
