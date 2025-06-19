import streamlit as st
import pandas as pd
import plotly.express as px
 
# Configuração inicial do Streamlit
st.set_page_config(layout="wide", page_title="Dashboard Campeonato Paulista")
 
# Caminho do arquivo CSV
# caminho_arquivo = r"C:\temp\Python\paulistao\campeonato_paulista_ranking_historico.csv"
caminho_arquivo = r"C:\Users\gabri\OneDrive\Documentos\GitHub\Dashboard-Campeonato-Paulista\campeonato_paulista_ranking_historico.csv"
# Inicializa o DataFrame
df = None
 
# Tenta carregar o arquivo CSV
try:
    df = pd.read_csv(caminho_arquivo, sep=";", decimal=",", encoding="latin1")
    # Exibe uma notificação temporária
    # st.toast("Arquivo carregado com sucesso!", icon="✅")
except FileNotFoundError:
    st.error("Arquivo não encontrado. Verifique o nome e o caminho.")
except PermissionError:
    st.error("Permissão negada. Feche o arquivo no Excel ou mova para outra pasta.")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
 
# Só continuar se o DataFrame foi carregado corretamente
if df is not None:
 
    # Filtros na barra lateral
    st.sidebar.title("Desenvolvido por:")
    st.sidebar.info("Cleiton Rodrigues, Douglas Mariano, Gabriel Roberto e Lysis Relvas")
    st.sidebar.title("Filtros")
 
# Filtro por time
if "Club" in df.columns:
    st.sidebar.markdown("### Filtro por Times")
   
    # Checkbox para selecionar todos os times
    selecionar_todos = st.sidebar.checkbox("Selecionar todos os times", value=True)
 
    if selecionar_todos:
        # Internamente, todos os times são selecionados, mas o campo do multiselect fica vazio
        times = df["Club"].unique()
        st.sidebar.multiselect(
            "Selecione os Times",
            df["Club"].unique(),
            default=[],
            disabled=True  # Desabilita o input quando "Selecionar todos" está marcado
        )
    else:
        # Permite seleção manual de times
        times = st.sidebar.multiselect(
            "Selecione os Times",
            df["Club"].unique(),
            default=[]
        )
 
    # Filtrar o DataFrame com base nos times selecionados
    df = df[df["Club"].isin(times)]
 
 
 
    # Filtro por participações
    if "Participations" in df.columns:
        df["Participations"] = pd.to_numeric(df["Participations"], errors="coerce")
        participations_valid = df["Participations"].dropna()
 
        if not participations_valid.empty:
            min_part = int(participations_valid.min())
            max_part = int(participations_valid.max())
 
            if min_part < max_part:
                participacoes_min = st.sidebar.slider(
                    "Quantidade de Participações no campeonato",
                    min_value=min_part,
                    max_value=max_part,
                    value=min_part
                )
                df = df[df["Participations"] >= participacoes_min]
            else:
                st.sidebar.info(
                    f"Todos os times têm {min_part} participações. Nenhum filtro necessário."
                )
                participacoes_min = min_part
        else:
            st.warning("Nenhum dado numérico válido encontrado na coluna 'Participations'.")
 
 
    # Título do dashboard
    st.title("Dashboard Campeonato Paulista")
 
    # Resumo de métricas
    total_pontos = df["Points"].sum() if "Points" in df.columns else 0
    total_partidas = df["Matches"].sum() if "Matches" in df.columns else 0
    total_gols = df["Goals_For"].sum() if "Goals_For" in df.columns else 0
 
    st.markdown("## Resumo")
    col1, col2, col3 = st.columns(3)
 
    with col1:
        st.metric(label="Total de Pontos", value=total_pontos)
 
    with col2:
        st.metric(label="Total de Partidas", value=total_partidas)
 
    with col3:
        st.metric(label="Total de Gols", value=total_gols)
 
 
# Listas de clubes por divisão
serie_a1 = [
    "Corinthians", "Palmeiras", "São Paulo", "Santos", "Portuguesa", "Guarani",
    "Ponte Preta", "Botafogo", "Ferroviária", "Mirassol", "Novorizontino",
    "São Bernardo FC", "Red Bull Bragantino", "Inter de Limeira", "São Caetano",
    "São José", "Ituano"
]
 
serie_a2 = [
    "Juventus", "América", "XV de Piracicaba", "São Bento", "Noroeste",
    "Portuguesa Santista", "Comercial-RP", "XV de Jaú", "Mogi Mirim",
    "Santo André", "Marília", "Paulista", "Paulistano", "Rio Branco",
    "Jabaquara", "União São João", "Taubaté", "Nacional", "SC Internacional",
    "AA São Bento", "Germânia", "Linense", "Comercial-SP", "AA das Palmeiras",
    "Araçatuba", "Oeste", "Sírio", "Francana", "União Barbarense",
    "Grêmio Barueri", "Prudentina", "Atlético Santista", "Guaratinguetá",
    "Auto", "Matonense"
]
 
serie_a3 = [
    "Velo Clube", "Red Bull", "São Bento-SCS", "São Paulo Athletic",
    "Mackenzie", "Americano", "Saad", "Rio Claro", "Grêmio Novorizontino",
    "Esportiva", "Taquaritinga", "Audax", "Catanduvense", "Sãocarlense",
    "Penapolense", "Olímpia", "Estudantes", "Antarctica", "CS América",
    "Atlético Sorocaba", "Sertãozinho", "Independência", "Radium",
    "Campos Elíseos", "Rio Preto", "São Caetano EC", "Bandeirante",
    "Luzitano", "Corinthians-PP"
]
 
serie_b = [
    "Água Santa", "Capivariano", "União Lapa", "Velo Clube", "Albion",
    "Independência/Sant'Anna", "CA Paulista", "Libanês", "Monte Azul",
    "Primeiro de Maio", "República", "Humberto I", "Grêmio Catanduvense",
    "Maranhão", "Alumni", "Jardim América", "Vicentino", "Scottish Wanderers",
    "Tremembé", "Ordem e Progresso", "Ítalo", "Corinthians-SBC",
    "Barra Funda", "SC Americano", "Paysandu", "Ruggerone", "Hydecroft",
    "CA Internacional", "Sant'Anna", "Britannia", "Independente EC"
]
 
# Normalizar os nomes na coluna "Club"
if "Club" in df.columns:
    df["Club"] = df["Club"].str.strip().str.lower()
    serie_a1_normalizado = [club.lower() for club in serie_a1]
    serie_a2_normalizado = [club.lower() for club in serie_a2]
    serie_a3_normalizado = [club.lower() for club in serie_a3]
    serie_b_normalizado = [club.lower() for club in serie_b]
 
    # Checkboxes para filtrar por divisões
    st.sidebar.markdown("### Filtro por Divisão")
    exibir_serie_a1 = st.sidebar.checkbox("Exibir Série A", value=False)
    exibir_serie_a2 = st.sidebar.checkbox("Exibir Série A2", value=False)
    exibir_serie_a3 = st.sidebar.checkbox("Exibir Série A3", value=False)
    exibir_serie_b = st.sidebar.checkbox("Exibir Série B", value=False)
 
    # Filtrar o DataFrame com base nos checkboxes
    if exibir_serie_a1:
        df = df[df["Club"].isin(serie_a1_normalizado)]
        st.success(f"Exibindo {len(df)} times da Série A.")
    elif exibir_serie_a2:
        df = df[df["Club"].isin(serie_a2_normalizado)]
        st.success(f"Exibindo {len(df)} times da Série A2.")
    elif exibir_serie_a3:
        df = df[df["Club"].isin(serie_a3_normalizado)]
        st.success(f"Exibindo {len(df)} times da Série A3.")
    elif exibir_serie_b:
        df = df[df["Club"].isin(serie_b_normalizado)]
        st.success(f"Exibindo {len(df)} times da Série B.")
    else:
        st.warning("Nenhuma divisão foi selecionada.")
   
    # Espaço para selecionar os gráficos desejados
st.sidebar.title("Gráficos")
st.sidebar.markdown("### Selecione os gráficos que deseja visualizar")
 
# Checkboxes para cada gráfico
exibir_gols_por_clube = st.sidebar.checkbox("Gols por Clube", value=True)
exibir_pontos_por_clube = st.sidebar.checkbox("Pontos por Clube", value=True)
exibir_participacoes_por_clube = st.sidebar.checkbox("Participações por Clube", value=False)
exibir_aproveitamento_por_clube = st.sidebar.checkbox("Aproveitamento por Clube", value=False)
exibir_distribuicao_de_gols = st.sidebar.checkbox("Distribuição de Gols", value=False)
exibir_clube_mais_gols = st.sidebar.checkbox("Clube com Mais Gols", value=False)
exibir_clube_mais_participacoes = st.sidebar.checkbox("Clube com Mais Participações", value=False)
exibir_clube_melhor_saldo = st.sidebar.checkbox("Clube com Melhor Saldo de Gols", value=False)
exibir_taxa_de_vitorias = st.sidebar.checkbox("Taxa de Vitórias", value=False)
 
# Gráficos
st.markdown("## Gráficos")
 
# Gráfico de Gols por Clube
if exibir_gols_por_clube and "Club" in df.columns and "Goals_For" in df.columns:
    fig_gols = px.bar(
        df,
        x="Club",
        y="Goals_For",
        color="Club",
        title="Gols Marcados por Clube",
        labels={"Goals_For": "Gols Marcados", "Club": "Clube"},
        text="Goals_For",
    )
    fig_gols.update_traces(textposition="outside")
    fig_gols.update_layout(
        xaxis_title="Clube",
        yaxis_title="Gols Marcados",
        showlegend=False,
        title_x=0.5,
    )
    st.plotly_chart(fig_gols, use_container_width=True, key="gols_por_clube")
   
 
# Gráfico de Pontos por Clube
if exibir_pontos_por_clube and "Club" in df.columns and "Points" in df.columns:
    fig_pontos = px.bar(
        df,
        x="Club",
        y="Points",
        color="Club",
        title="Pontos por Clube",
        labels={"Points": "Pontos", "Club": "Clube"},
        text="Points",
    )
    fig_pontos.update_traces(textposition="outside")
    fig_pontos.update_layout(
        xaxis_title="Clube",
        yaxis_title="Pontos",
        showlegend=False,
        title_x=0.5,
    )
    st.plotly_chart(fig_pontos, use_container_width=True, key="pontos_por_clube")
 
# Gráfico de Participações por Clube
if exibir_participacoes_por_clube and "Club" in df.columns and "Participations" in df.columns:
    if len(df) > 1:
        fig_participacoes = px.pie(
            df,
            names="Club",
            values="Participations",
            title="Participações por Clube",
            labels={"Participations": "Participações", "Club": "Clube"},
        )
        fig_participacoes.update_layout(title_x=0.5)
        st.plotly_chart(fig_participacoes, use_container_width=True, key="participacoes_por_clube")
    elif len(df) == 1:
        st.warning("O gráfico de pizza requer pelo menos dois times para ser exibido.")
 
# Gráfico de Aproveitamento por Clube
if exibir_aproveitamento_por_clube and {"Won", "Drawn", "Lost"}.issubset(df.columns):
    fig_aproveitamento = px.bar(
        df,
        x="Club",
        y=["Won", "Drawn", "Lost"],
        title="Aproveitamento por Clube (Vitórias, Empates e Derrotas)",
        labels={"value": "Partidas", "variable": "Resultado", "Club": "Clube"},
    )
    fig_aproveitamento.update_layout(barmode="stack", xaxis_title="Clube", yaxis_title="Número de Partidas", title_x=0.5)
    st.plotly_chart(fig_aproveitamento, use_container_width=True, key="aproveitamento_por_clube")
 
# Gráfico de Distribuição de Gols
if exibir_distribuicao_de_gols and "Goals_For" in df.columns:
    fig_distribuicao_gols = px.histogram(
        df,
        x="Goals_For",
        nbins=20,
        title="Distribuição de Gols Marcados pelos Clubes",
        labels={"Goals_For": "Gols Marcados"},
    )
    fig_distribuicao_gols.update_layout(xaxis_title="Gols Marcados", yaxis_title="Frequência", title_x=0.5)
    st.plotly_chart(fig_distribuicao_gols, use_container_width=True, key="distribuicao_de_gols")
 
# Métricas adicionais
if exibir_clube_mais_gols and "Goals_For" in df.columns:
    clube_mais_gols = df.loc[df["Goals_For"].idxmax(), "Club"]
    gols_mais_gols = df["Goals_For"].max()
    st.metric(label="Clube com Mais Gols", value=f"{clube_mais_gols} ({gols_mais_gols} gols)")
 
if exibir_clube_mais_participacoes and "Participations" in df.columns:
    clube_mais_participacoes = df.loc[df["Participations"].idxmax(), "Club"]
    participacoes_mais = df["Participations"].max()
    st.metric(label="Clube com Mais Participações", value=f"{clube_mais_participacoes} ({participacoes_mais} vezes)")
 
if exibir_clube_melhor_saldo and "Goals_Difference" in df.columns:
    clube_melhor_saldo = df.loc[df["Goals_Difference"].idxmax(), "Club"]
    melhor_saldo = df["Goals_Difference"].max()
    st.metric(label="Clube com Melhor Saldo de Gols", value=f"{clube_melhor_saldo} ({melhor_saldo})")
 
if exibir_taxa_de_vitorias and {"Won", "Matches"}.issubset(df.columns):
    df["Win_Rate"] = (df["Won"] / df["Matches"]) * 100
    fig_taxa_vitorias = px.bar(
        df,
        x="Club",
        y="Win_Rate",
        title="Taxa de Vitórias por Clube (%)",
        labels={"Win_Rate": "Taxa de Vitórias (%)", "Club": "Clube"},
        text="Win_Rate",
    )
    fig_taxa_vitorias.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig_taxa_vitorias.update_layout(xaxis_title="Clube", yaxis_title="Taxa de Vitórias (%)", title_x=0.5)
    st.plotly_chart(fig_taxa_vitorias, use_container_width=True, key="taxa_de_vitorias")
   
# steamlit run dashboard_Fut.py