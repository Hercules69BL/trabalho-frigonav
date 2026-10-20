
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import textwrap

csv_data = """ID;Código;Categoria;Tipo de Carne;Corte;Peso (kg);Preço Custo (R$);Preço Venda (R$);Quantidade;Data Entrada;Data Validade;Status;Revisar
1;BOV001;Bovina;Carne Bovina;Picanha;2000;0.06;10.05;15;2026-05-10;2026-05-25;Erro;Peso e custo suspeitos
2;BOV002;Frango;Carne de Frango;Peito de Frango;18;35.50;57.90;20;2026-05-11;2026-05-26;Em estoque;
3;BOV003;Bovina;Carne Bovina;Contra-filé;20;38.00;61.90;12;2026-05-12;2026-05-27;Em estoque;
4;SUN001;Suína;Carne Suína;Costela Suína;10;22.00;39.90;18;2026-05-09;2026-05-22;Em estoque;
5;SUN002;Suína;Carne Suína;Pernil;25;19.50;34.90;30;2026-05-08;2026-05-23;Em estoque;
6;FRG001;Frango;Carne de Frango;Peito de Frango;30;14.00;24.90;-70;2026-05-13;2026-05-20;Erro;Quantidade negativa
7;FRG002;Frango;Carne de Frango;Coxa e Sobrecoxa;22;11.50;700.50;35;2026-05-13;2026-05-21;Em estoque;Preço de venda suspeito
8;SUN003;Suína;Carne Suína;Costelinha;14;20.50;25.50;45;2026-05-12;2026-05-23;Em estoque;
9;BOV004;Bovina;Carne Bovina;Acém;16;24.00;42.90;10;2026-05-12;2026-05-28;Em estoque;
10;EMB001;Embutidos;Linguiça Toscana;Toscana Artesanal;500.09;17.00;31.90;25;2026-05-11;2026-05-30;Em estoque;Peso e unidade suspeitos
11;SUN004;Suína;Carne Suína;Picanha;16.5;40.00;45.00;;2026-05-14;2026-05-25;Erro;Quantidade ausente
12;BOV009;Embutidos;Salame;Salame Italiano;18;29.00;48.90;15;2026-05-20;2026-06-01;Em estoque;Conferir código e categoria
13;BOV010;Bovina;Carne Bovina;Costela Bovina;30;23.50;41.90;18;2026-05-21;2026-06-03;Em estoque;
14;SUN008;Suína;Carne Suína;Pé Suíno;12;11.00;19.90;22;2026-05-21;2026-05-29;Em estoque;
15;FRG007;Frango;Carne de Frango;Coração de Frango;9;13.50;24.50;9999999;2026-05-22;2090-05-28;Erro;Quantidade e validade suspeitas
16;EMB005;Embutidos;Linguiça Apimentada;Toscana Picante;15;18.50;34.90;20;2026-05-22;2026-06-04;Em estoque;
17;BOV011;Bovina;Carne Bovina;Músculo;21;22.00;39.90;25;2026-05-23;2026-06-02;Em estoque;
18;SUN009;Suína;Carne Suína;Costela Defumada;17;27.00;46.90;14;2026-05-23;2026-05-31;Em estoque;
19;FRG008;Frango;Carne de Frango;Filé de Frango;26;16.00;28.90;30;2026-05-24;2026-05-30;Em estoque;
20;EMB006;Embutidos;Carne de Frango;Linguiça de Frango;999.09;0.05;21.90;35;2026-05-24;2026-06-06;Em estoque;Peso e custo suspeitos
21;BOV012;Bovina;Carne Bovina;Filé Mignon;10;58.00;89.90;8;2026-05-25;2026-06-01;Em estoque;
22;SUN010;Suína;Carne Suína;Joelho Suíno;13;15.00;27.90;19;2026-05-25;2026-06-02;Em estoque;
23;FRG009;Frango;Carne de Frango;Sobrecoxa Desossada;20;14.50;25.90;27;2026-05-26;2026-06-01;Em estoque;
24;EMB007;Embutidos;Salame;Salame Italiano;8;35.00;59.90;12;2026-05-26;2026-06-10;Em estoque;
25;BOV013;Bovina;Carne Bovina;Rabada;19;20.00;36.90;21;2026-05-27;2026-06-05;Em estoque;
26;FRG010;Frango;Carne de Frango;Frango Caipira;28;18.00;32.90;18;2026-05-27;2026-06-03;Em estoque;
27;BOV005;Bovina;Carne Bovina;Maminha;15;36.00;59.90;18;2026-05-15;2026-05-29;Em estoque;
28;BOV006;Bovina;Carne Bovina;Fraldinha;17.5;33.50;55.90;16;2026-05-15;2026-05-30;Em estoque;
29;SUN005;Suína;Carne Suína;Lombo Suíno;20;21.00;37.90;22;2026-05-14;2026-05-26;Em estoque;
30;FRG003;Frango;Carne de Frango;Asa de Frango;18;10.00;18.90;28;2026-05-16;2026-05-22;Em estoque;
31;FRG004;Frango;Carne de Frango;Filezinho Sassami;12;15.50;27.90;14;2026-05-16;2026-05-23;Em estoque;
32;EMB002;Frango;Carne de Frango;Sambiquira;10;16.00;29.90;26;2026-05-12;2026-06-02;Em estoque;Conferir código e categoria
33;BOV007;Bovina;Carne Bovina;Cupim;13;28.00;49.90;11;2026-05-17;2026-05-31;Em estoque;
34;SUN006;Suína;Carne Suína;Paleta Suína;19;18.50;32.90;24;2026-05-17;2026-05-28;Em estoque;
35;FRG005;Frango;Carne de Frango;Frango Inteiro;35;9.50;16.90;-3;2026-05-18;2026-05-24;Erro;Quantidade negativa
36;EMB003;Embutidos;Carne Suína;Calabresa;20;12.00;19.90;30;2026-05-18;2026-06-05;Em estoque;Conferir classificação
37;BOV008;Bovina;Carne Bovina;Patinho;14;31.00;53.90;13;2026-05-18;2026-05-30;Em estoque;
38;SUN007;Suína;Carne Suína;Torresmo;8;25.00;44.90;12;2026-05-19;2026-05-27;Em estoque;
39;FRG006;Frango;Carne de Frango;Moela;11;8.50;999.99;99;2026-05-19;2026-05-25;Em estoque;Preço de venda suspeito
40;EMB004;Embutidos;Salame;Salame Italiano;13;18.00;33.90;17;2026-05-20;2026-06-08;Em estoque;"""

df = pd.read_csv(StringIO(csv_data), sep=";")
df.columns = df.columns.str.strip()

colunas_numericas = [
    "Peso (kg)",
    "Preço Custo (R$)",
    "Preço Venda (R$)",
    "Quantidade"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(df[coluna], errors="coerce")

for coluna in ["Data Entrada", "Data Validade"]:
    df[coluna] = pd.to_datetime(df[coluna], errors="coerce")

sns.set_theme(style="whitegrid", palette="Set2")

fig, axes = plt.subplots(2, 3, figsize=(19, 12))

fig.suptitle(
    "ANÁLISE DO ESTOQUE DE CARNES",
    fontsize=20,
    fontweight="bold"
)

categorias = df["Categoria"].value_counts()

axes[0, 0].bar(
    categorias.index,
    categorias.values,
    color=sns.color_palette("Set2", len(categorias))
)

axes[0, 0].set_title("1. Produtos por categoria")
axes[0, 0].set_xlabel("Categoria")
axes[0, 0].set_ylabel("Quantidade de registros")
axes[0, 0].tick_params(axis="x", rotation=25)

for i, valor in enumerate(categorias.values):
    axes[0, 0].text(i, valor + 0.2, str(valor), ha="center")

precos_validos = df[
    df["Preço Custo (R$)"].between(0, 100)
    & df["Preço Venda (R$)"].between(0, 100)
].copy()

top10 = precos_validos.nlargest(
    10, "Preço Venda (R$)"
).sort_values("Preço Venda (R$)")

posicoes = range(len(top10))

axes[0, 1].barh(
    list(posicoes),
    top10["Preço Custo (R$)"],
    color="#4C78A8",
    label="Preço de custo"
)

axes[0, 1].barh(
    list(posicoes),
    top10["Preço Venda (R$)"],
    color="#F58518",
    alpha=0.8,
    label="Preço de venda"
)

axes[0, 1].set_yticks(list(posicoes))
axes[0, 1].set_yticklabels(top10["Corte"])
axes[0, 1].set_title("2. Custo x venda — 10 produtos")
axes[0, 1].set_xlabel("Preço (R$)")
axes[0, 1].legend()

status = df["Status"].fillna("Não informado").value_counts()

axes[0, 2].pie(
    status.values,
    labels=status.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#E45756", "#72B7B2", "#B279A2"][:len(status)]
)

axes[0, 2].set_title("3. Registros por status")

pesos_validos = df[df["Peso (kg)"].between(0, 100)]

peso_categoria = (
    pesos_validos.groupby("Categoria")["Peso (kg)"]
    .sum()
    .sort_values()
)

axes[1, 0].barh(
    peso_categoria.index,
    peso_categoria.values,
    color="#72B7B2"
)

axes[1, 0].set_title("4. Peso por categoria")
axes[1, 0].set_xlabel("Peso total (kg)")

erros = df[
    df["Revisar"].notna()
    & df["Revisar"].astype(str).str.strip().ne("")
]

erros_resumo = erros["Revisar"].value_counts().sort_values()

rotulos = [
    textwrap.fill(str(rotulo), width=28)
    for rotulo in erros_resumo.index
]

axes[1, 1].barh(
    rotulos,
    erros_resumo.values,
    color="#E45756"
)

axes[1, 1].set_title("5. Inconsistências encontradas")
axes[1, 1].set_xlabel("Número de registros")

for i, valor in enumerate(erros_resumo.values):
    axes[1, 1].text(valor + 0.03, i, str(valor), va="center")

axes[1, 2].axis("off")

total = len(df)
com_erro = (df["Status"] == "Erro").sum()
em_estoque = (df["Status"] == "Em estoque").sum()

quantidades_suspeitas = (
    df["Quantidade"].isna()
    | (df["Quantidade"] < 0)
    | (df["Quantidade"] > 10000)
).sum()

resumo = (
    "RESUMO DO ESTOQUE\n\n"
    f"Total de registros: {total}\n"
    f"Registros com erro: {com_erro}\n"
    f"Registros em estoque: {em_estoque}\n"
    f"Quantidades ausentes/suspeitas: {quantidades_suspeitas}\n\n"
    "Observação:\n"
    "Valores extremos foram filtrados\n"
    "somente nos gráficos que precisam\n"
    "dessa limitação."
)

axes[1, 2].text(
    0.05,
    0.95,
    resumo,
    va="top",
    ha="left",
    fontsize=12,
    bbox=dict(
        boxstyle="round,pad=0.7",
        facecolor="#F2F2F2",
        edgecolor="#CCCCCC"
    )
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig(
    "graficos_estoque_carnes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Os gráficos foram gerados com sucesso!")
print("Imagem salva como: graficos_estoque_carnes.png")