import matplotlib
matplotlib.use('Agg')

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

def gerar_grafico():

    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    
    if not os.path.exists('data'):
        os.makedirs('data')

    df = pd.read_excel(
        "data/Remuneracao_docentes_Municipios_2020.xlsx",
        sheet_name="MUNICÍPIO",
        engine='openpyxl',
        skiprows=8
    )

    colunas_renomeadas = {
        'NU_ANO_CENSO': 'ano',
        'NO_REGIAO': 'regiao',
        'SG_UF': 'uf',
        'CO_MUNICIPIO': 'cod_municipio',
        'NO_MUNICIPIO': 'municipio',
        'NO_DEPENDENCIA': 'dependencia',
        'NO_CATEGORIA': 'escolaridade',
        'ED_BAS_CAT1': 'num_docentes',
        'ED_BAS_CAT2': 'perc_rais',
        'ED_BAS_CAT3': 'remuneracao_q1',
        'ED_BAS_CAT4': 'remuneracao_mediana',
        'ED_BAS_CAT5': 'remuneracao_media',
        'ED_BAS_CAT6': 'remuneracao_q3',
        'ED_BAS_CAT7': 'remuneracao_desvio_padrao',
        'ED_BAS_CAT8': 'carga_horaria_media',
        'ED_BAS_CAT9': 'remuneracao_40h'
    }
    df = df.rename(columns=colunas_renomeadas)
    df = df[~df['remuneracao_media'].isin(['a', 'd'])]

    cols_numericas = [
        'remuneracao_media',
        'carga_horaria_media',
        'remuneracao_40h',
        'remuneracao_q1',
        'remuneracao_mediana',
        'remuneracao_q3',
        'remuneracao_desvio_padrao',
        'perc_rais'
    ]
    print(df.info())  
    print(df.describe())
    print("Valores únicos na coluna 'escolaridade':", df['escolaridade'].unique())

    df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric, errors='coerce')

    df_municipal = df[df['dependencia'] == 'Municipal']

    df_municipal_cleaned = df_municipal.dropna(subset=['remuneracao_media'])

    media_uf = df_municipal_cleaned.groupby('uf')['remuneracao_media'].mean().reset_index()
    media_uf = media_uf.sort_values(by='remuneracao_media', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=media_uf, x='uf', y='remuneracao_media', hue='uf', palette='viridis', legend=False)
    plt.title('Remuneração Média de Docentes Municipais por UF (2020)')
    plt.xlabel('UF')
    plt.ylabel('Remuneração Média (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/remuneracao_por_uf.png') 
    plt.close()

    # Número de Docentes por UF
    num_docentes_por_uf = df_municipal_cleaned.groupby('uf')['num_docentes'].sum().reset_index()
    num_docentes_por_uf = num_docentes_por_uf.sort_values(by='num_docentes', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=num_docentes_por_uf, x='uf', y='num_docentes', hue='uf', palette='viridis', legend=False)
    plt.title('Número de Docentes por UF (2020)')
    plt.xlabel('UF')
    plt.ylabel('Número de Docentes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/num_docentes_por_uf.png')
    plt.close()

    # Número de Docentes por Escolaridade
    num_docentes_por_escolaridade = df_municipal_cleaned.groupby('escolaridade')['num_docentes'].sum().reset_index()
    num_docentes_por_escolaridade = num_docentes_por_escolaridade.sort_values(by='num_docentes', ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=num_docentes_por_escolaridade, x='escolaridade', y='num_docentes', palette='viridis', legend=False)
    plt.title('Número de Docentes por Escolaridade (2020)')
    plt.xlabel('Nível de Escolaridade')
    plt.ylabel('Número de Docentes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/num_docentes_por_escolaridade.png')
    plt.close()

    df.to_csv('data/dados_tratados_para_powerbi.csv', index=False)

    # Número de Docentes Escolarizados por UF (Ensino Superior)
    df_escolarizados = df_municipal_cleaned[df_municipal_cleaned['escolaridade'] == 'Superior']
    num_docentes_escolarizados_por_uf = df_escolarizados.groupby('uf')['num_docentes'].sum().reset_index()
    num_docentes_escolarizados_por_uf = num_docentes_escolarizados_por_uf.sort_values(by='num_docentes', ascending=False)

    # Gráfico de Número de Docentes Escolarizados por UF (Ensino Superior)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=num_docentes_escolarizados_por_uf, x='uf', y='num_docentes', palette='viridis', legend=False)
    plt.title('Número de Docentes Escolarizados por UF (Ensino Superior) (2020)')
    plt.xlabel('UF')
    plt.ylabel('Número de Docentes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/num_docentes_escolarizados_por_uf.png')
    plt.close()

@app.route('/')
def index():
    gerar_grafico()  
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
