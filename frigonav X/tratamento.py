import pandas as pd

df = pd.read_csv("dados.csv")

print(df.head())

print(df.shape)


print(df.columns)


print(df.dtypes)


df.info()


print(df.isnull().sum())

df.columns = df.columns.str.strip()

print(df.columns)

colunas_texto = [
    "Código",
    "Categoria",
    "Tipo de Carne",
    "Corte",
    "Status"
]

for coluna in colunas_texto:
    df[coluna] = (
        df[coluna]
        .astype("string")
        .str.strip()
    )

    df["Status"] = df["Status"].replace({
    "erro": "Erro",
    "Em estoque": "Em estoque",
    "Baixo estoque": "Baixo estoque"
})
    
    colunas_numericas = [
    "ID",
    "Peso (kg)",
    "Preço Custo (R$)",
    "Preço Venda (R$)",
    "Quantidade"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

    df["Data Entrada"] = pd.to_datetime(
    df["Data Entrada"],
    errors="coerce"
)

df["Data Validade"] = pd.to_datetime(
    df["Data Validade"],
    errors="coerce"
)

print(df[["Data Entrada", "Data Validade"]].head())

print(df.isnull().sum())

print(df[df.isnull().any(axis=1)])

print("Duplicados:", df.duplicated().sum())

print(df[df["Quantidade"] < 0])


print(df[df["Quantidade"] > 10000])


print(df[df["Quantidade"].isna()])

print(df[df["Preço Custo (R$)"] < 1])

# Venda superior a R$ 200
print(df[df["Preço Venda (R$)"] > 200])

# Venda abaixo do custo
print(
    df[
        df["Preço Venda (R$)"]
        < df["Preço Custo (R$)"]
    ]
)

df["Revisar"] = ""

df.loc[
    df["Quantidade"].isna()
    | (df["Quantidade"] < 0),
    "Revisar"
] = "Verificar quantidade"

df.loc[
    df["Preço Custo (R$)"].isna()
    | (df["Preço Custo (R$)"] <= 0),
    "Revisar"
] = "Verificar preço de custo"

print(df[df["Revisar"] != ""])

df.to_csv(
    "dados_tratados.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Dados tratados e salvos com sucesso!")