# Trabalho Individual - Análise de Conjunto de Dados Educacionais

## Objetivo

Este trabalho tem como objetivo aplicar os conceitos aprendidos em sala de aula, utilizando bibliotecas Python para analisar um conjunto de dados educacionais do portal do **INEP** (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira). Você deverá realizar uma análise básica dos dados e seguir os passos descritos abaixo, utilizando técnicas de **data wrangling**, **visualização de dados** e **operações de agregação**.

## Instruções

1. **Escolha do Conjunto de Dados:**

   * Selecione um conjunto de dados educacionais disponível no portal do INEP, **exceto aquele já explorado em aula**.
   * O conjunto de dados pode ser relacionado a indicadores educacionais como taxas de escolaridade, desempenho dos alunos, infraestrutura escolar, etc.

2. **Descrição do Conjunto de Dados:**

   * Faça uma breve descrição do conjunto de dados selecionado, abordando o que ele representa, suas fontes e o que cada coluna significa.

3. **Procedimentos:**

   * **Leitura do Arquivo:** Utilize métodos adequados para ler o arquivo. Caso o arquivo seja `.csv`, `.xlsx`, ou outro formato, utilize as bibliotecas Python apropriadas para carregá-lo no ambiente.

   * **Data Wrangling:**

     * Selecione atributos relevantes para a análise.
     * Realize o tratamento de valores faltantes ou inconsistentes (como valores `NaN`, valores duplicados, ou dados fora do padrão esperado).

   * **Exploração dos Dados:**

     * Utilize os métodos `info()` e `describe()` para entender a estrutura dos dados e as características das variáveis.
     * Interprete de forma sucinta as saídas desses métodos, destacando os pontos mais importantes.

   * **Operações de Agregação:**

     * Utilize o método `groupby()` para realizar agregações (por exemplo, média de notas por estado, contagem de escolas por categoria, etc.).

   * **Visualização de Dados:**

     * Gere gráficos que ajudem a entender os padrões e tendências do conjunto de dados, utilizando bibliotecas como `matplotlib`, `seaborn` ou `plotly`.

   * **Exportação dos Dados:**

     * Após o tratamento e análise dos dados, exporte o conjunto de dados tratado para um arquivo **CSV**, que será importado no Power BI.

   * **Criação de Dashboard no Power BI:**

     * Importe o arquivo **CSV** tratado para o Power BI.
     * Crie um dashboard simples para apresentação dos resultados de sua análise.

4. **Entrega:**

   * Submeta o **notebook no Colab** ou **repositório GitHub** contendo o código da análise.
   * Anexe o **arquivo do Power BI** com o dashboard criado para apresentação dos resultados.
   * O arquivo do Power BI deve conter as visualizações relevantes para a análise dos dados, e os resultados devem ser apresentados de forma clara e objetiva.

## Avaliação

A avaliação será baseada na execução correta dos seguintes procedimentos:

* Leitura e descrição do conjunto de dados.
* Aplicação de técnicas de **data wrangling** (tratamento de dados).
* Uso correto de **agregações com `groupby`**.
* Criação de **visualizações relevantes** para a análise.
* Exportação correta dos dados tratados e criação de um **dashboard funcional no Power BI**.

## Observações

* **Foco principal:** O objetivo deste trabalho é demonstrar sua capacidade de aplicar os métodos e bibliotecas Python vistas em aula, e não realizar uma análise aprofundada ou explorar todas as possíveis interpretações dos dados.
* **Não se preocupe com a perfeição dos resultados**, mas sim com a execução correta dos procedimentos.


Aqui está o passo a passo para configurar o ambiente de desenvolvimento com as bibliotecas necessárias, incluindo a criação do **venv** (ambiente virtual) e a instalação das dependências a partir do **requirements.txt**:

---
Aqui está o passo a passo completo, agora incluindo o comando para executar o Flask (`app.py`) após ativar o ambiente virtual e acessar o diretório `analise_proj`.

---

### Passo a Passo Completo para Configuração do Ambiente e Execução do Flask

#### 1. **Criar o Ambiente Virtual (`venv`)**

##### Para Windows:

1. **Abra o terminal ou prompt de comando**.
2. Navegue até o diretório do projeto onde você deseja criar o ambiente virtual.
3. Execute o seguinte comando para criar o ambiente virtual:

   ```bash
   python -m venv venv
   ```

##### Para macOS/Linux:

1. **Abra o terminal**.
2. Navegue até o diretório do projeto onde você deseja criar o ambiente virtual.
3. Execute o seguinte comando para criar o ambiente virtual:

   ```bash
   python3 -m venv venv
   ```

#### 2. **Instalar as Dependências a partir do `requirements.txt`**

1. **Ative o ambiente virtual**:

   ##### Para Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   ##### Para macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

2. Com o ambiente virtual ativado, instale as dependências com o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

#### 3. **Entrar no Diretório do Projeto**

1. Depois de ativar o ambiente virtual, **acessa o diretório do projeto** onde está o seu arquivo `app.py`.

   * No seu caso, o diretório é `analise_proj`, então faça isso:

   ```bash
   cd analise_proj
   ```

#### 4. **Executar o Aplicativo Flask**

1. Agora, você pode **executar o aplicativo Flask**. No diretório `analise_proj`, execute o seguinte comando:

   ```bash
   python app.py
   ```

2. O Flask irá iniciar o servidor de desenvolvimento e você verá uma saída como esta no terminal:

   ```
   * Serving Flask app 'app'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 463-049-529
   ```

3. **Acesse o aplicativo** no navegador:

   * Abra o navegador e vá até **[http://127.0.0.1:5000](http://127.0.0.1:5000)** para visualizar o aplicativo rodando localmente.

#### 5. **Desativar o Ambiente Virtual**

1. Quando terminar de trabalhar, você pode **desativar o ambiente virtual** com o comando:

   ```bash
   deactivate
   ```

---

### Resumo

1. **Criar o ambiente virtual**:

   * Windows: `python -m venv venv`
   * macOS/Linux: `python3 -m venv venv`

2. **Ativar o ambiente virtual**:

   * Windows: `.\venv\Scripts\activate`
   * macOS/Linux: `source venv/bin/activate`

3. **Instalar as dependências**: `pip install -r requirements.txt`

4. **Acessar o diretório do projeto**:

   ```bash
   cd analise_proj
   ```

5. **Executar o Flask**:

   ```bash
   python app.py
   ```

6. **Acessar o servidor**: Abra o navegador e vá até `http://127.0.0.1:5000`.

7. **Desativar o ambiente virtual**: `deactivate`



