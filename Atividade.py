#%%
import pandas as pd

#%%
#1) carregar a base de dados: base_carros_usados.csv
carros = pd.read_csv('base_carros_usados.csv')

#%%
#2) exibir a estrutura das variáveis (colunas).
carros.info()

#%%
#3) alterar a descrição da coluna (renomear as colunas) para o idioma português brasileiro
#não utilizar espaços nem acentos
#exibir a estrutura das variáveis após a alteração

carros.rename(columns={    
    'car_name' : 'nome_carro', 
    'brand': 'marca', 
    'model': 'modelo', 
    'new_price': 'novo_preco', 
    'min cost_price':'preco_minimo',
    'max_cost_price':'preco_maximo', 
    'vehicle age':'idade_veiculo', 
    'km_driven':'km_rodados', 
    'seller_type': 'tipo_vendedor',
    'fuel_type':'tipo_combustivel', 
    'transmission_type':'tipo_transmissao', 
    'mileage':'milhas', 
    'engine':'motor', 
    'max power':'potencia_maxima',
    'seats':'assentos', 
    'selling price':'preco_venda'
    },
    inplace=True)

#%%
#4)detalhar o dicionário dos dados (fazer uma tabela com o nome de cada coluna, tipo e a descrição
#dos dados que a mesma contém)

dicionario_dados = [
    {'Coluna': 'id', 'Tipo da variável': 'Quantitativa discreta', 'Descrição': 'Identificador único do carro'},
    {'Coluna': 'nome_carro', 'Tipo da variável': 'Qualitativa nominal', 'Descrição': 'Nome do carro'},
    {'Coluna': 'marca', 'Tipo da variável': 'Qualitativa nominal', 'Descrição': 'Marca do carro'},
    {'Coluna': 'modelo', 'Tipo da variável': 'Qualitativa nominal', 'Descrição': 'Modelo do carro'},
    {'Coluna': 'preco_novo', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Preço do carro novo'},
    {'Coluna': 'preco_custo_minimo', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Preço de custo mínimo do carro'},
    {'Coluna': 'preco_custo_maximo', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Preço de custo máximo do carro'},
    {'Coluna': 'idade_veiculo', 'Tipo da variável': 'Quantitativa discreta', 'Descrição': 'Idade do veículo em anos'},
    {'Coluna': 'km_rodados', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Quilometragem rodada pelo carro'},
    {'Coluna': 'tipo_vendedor', 'Tipo da variável': 'Qualitativa categórica', 'Descrição': 'Tipo de vendedor (particular, revenda)'},
    {'Coluna': 'tipo_combustivel', 'Tipo da variável': 'Qualitativa categórica', 'Descrição': 'Tipo de combustível utilizado pelo carro'},
    {'Coluna': 'tipo_transmissao', 'Tipo da variável': 'Qualitativa categórica', 'Descrição': 'Tipo de transmissão (manual, automática)'},
    {'Coluna': 'quilometragem', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Consumo de combustível por quilômetro rodado'},
    {'Coluna': 'motor', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Capacidade do motor em litros'},
    {'Coluna': 'potencia_maxima', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Potência máxima do carro em cavalos (HP)'},
    {'Coluna': 'assentos', 'Tipo da variável': 'Quantitativa discreta', 'Descrição': 'Número de assentos no carro'},
    {'Coluna': 'preco_venda', 'Tipo da variável': 'Quantitativa contínua', 'Descrição': 'Preço de venda do carro em reais'}
]
dicionario_df = pd.DataFrame(dicionario_dados)
#%%
#5) exibir as 5 primeiras linhas do dafaframe, use head(5)
carros.head(5)

#%%#6) exibir as 5 últimas linhas do dafaframe, use tail (5)
carros.tail(5)

#%%#7) verificar se a base de dados contém NaN e tratá-los. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
carros.isnull().sum()
carros['marca'].value_counts()
# preenche os NaNs de 'novo_preco' como 'Novo preco nao informado', por estar em moeda diferente 
# e termos outras metricas de precificacao, sera dispensavel
carros['novo_preco'] = carros['novo_preco'].fillna('Novo preco nao informado')


marcas = ["Maruti", "Hyundai", "Honda", "Mahindra", "Toyota", "Tata", "Ford", "Volkswagen",
          "Renault", "Mercedes-Benz", "BMW", "Skoda", "Chevrolet", "Audi", "Nissan", 
          "Datsun", "Fiat", "Jaguar", "Land Rover", "Volvo", "Jeep", "Mitsubishi", 
          "Kia", "Porsche", "Mini", "MG", "Isuzu", "Lexus", "Force", "Bentley", 
          "Ambassador", "OpelCorsa", "ISUZU", "DC", "Maserati", "Daewoo", 
          "Premier", "Lamborghini", "Ferrari", "Mercedes-AMG", "Rolls-Royce", "Opel"]

# Calcular a média dos preços mínimos para cada marca
media_preco_minimo_por_marca = carros.groupby('marca')['preco_minimo'].mean()

# Atualizar valores faltantes com a média correspondente
for marca in marcas:
    if marca in media_preco_minimo_por_marca.index:
        carros.loc[carros['marca'] == marca, 'preco_minimo'] = carros.loc[carros['marca'] == marca, 'preco_minimo'].fillna(media_preco_minimo_por_marca[marca])

media_preco_maximo_por_marca = carros.groupby('marca')['preco_maximo'].mean()
# Atualizar valores faltantes com a média correspondente
for marca in marcas:
    if marca in media_preco_maximo_por_marca.index:
        carros.loc[carros['marca'] == marca, 'preco_maximo'] = carros.loc[carros['marca'] == marca, 'preco_maximo'].fillna(media_preco_maximo_por_marca[marca])

carros = carros.dropna()
carros.reset_index(drop=True, inplace=True)

#%% #8) excluindo colunas desnecessárias, justifique a exclusão.
# Remover colunas desnecessárias
carros.drop(columns=['nome_carro','novo_preco', 'assentos', 'milhas', 'motor', 'preco_maximo'], inplace=True) 

#%% #9) excluindo todas as linhas dos carros da marca 'Tata'
#reseta o indice (isso é necessário devido as exclusões das linhas)

# Encontrar os índices das linhas onde a marca é 'Tata'
indices_tata = carros[carros['marca'] == 'Tata'].index

# Excluir essas linhas
carros = carros.drop(indices_tata)

# Redefinir o índice do DataFrame
carros.reset_index(drop=True, inplace=True)
#%%#10) alterando dados das informações da coluna 'tipo_vendedor':
#De 'Individual' de 'particular'
#De 'Trustmark Dealer de 'concessionária'
#De 'Dealer' de 'distribuidora'

carros['tipo_vendedor'] = carros['tipo_vendedor'].replace({
    'Individual': 'particular',
    'Trustmark Dealer': 'concessionária',
    'Dealer': 'distribuidora'
})
#%%
carros['preco_minimo'] = carros['preco_minimo'].astype(float)
carros['ipva'] = carros['ipva'].astype(float)

#%%
#11) crie uma nova coluna denominada ipva e calcule:
#Para carros com menos de 20 anos: o ipva é 4% do valor do carro
#Carros com 20 anos ou mais é isento de ipva
carros['ipva'] = 0.0

carros['preco_minimo'] = carros['preco_minimo'].astype(float)
carros['ipva'] = carros['ipva'].astype(float)
# Atualizar o IPVA para carros com menos de 20 anos
carros.loc[carros['idade_veiculo'] < 20, 'ipva'] = carros['preco_venda'] * 0.04
#%%#12) crie novas colunas que julgue pertinente ao seu estudo, justifique.

carros['ano'] = 2024- carros['idade_veiculo']
# Inicializar a coluna 'estado' com valores nulos
carros['estado'] = None

# Atualizar a coluna 'estado' com base nos valores de 'km_rodados'
carros.loc[carros['km_rodados'] < 30000, 'estado'] = "novo"
carros.loc[(carros['km_rodados'] >= 30000) & (carros['km_rodados'] < 80000), 'estado'] = "moderadamente rodado"
carros.loc[carros['km_rodados'] >= 80000, 'estado'] = "rodado"

#%%
#13) gravar o novo dataframe, com nome “carros_usados_atualizado.csv”

carros.to_csv('carros_usados_atualizado.csv')

#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
