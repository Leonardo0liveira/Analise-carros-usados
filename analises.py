#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%

carros_atualizado= pd.read_csv('carros_usados_atualizado.csv')
#%%
freq_marca = carros_atualizado['marca'].value_counts()
freq_preco_minimo = carros_atualizado['preco_minimo'].value_counts()
freq_idade = carros_atualizado['idade_veiculo'].value_counts()
freq_tipo_vendedor = carros_atualizado['tipo_vendedor'].value_counts()
freq_tipo_combustivel = carros_atualizado['tipo_combustivel'].value_counts()
freq_tipo_transmissao = carros_atualizado['tipo_transmissao'].value_counts()
freq_potencia_max = carros_atualizado['potencia_maxima'].value_counts()
freq_preco_venda = carros_atualizado['preco_venda'].value_counts()
freq_ipva = carros_atualizado['ipva'].value_counts()
#%%
freq_estado = carros_atualizado['estado'].value_counts()
#%%

freq_marca.head(11).plot.bar(title="frequencia de marcas", rot=45, color='red', figsize=(10,6))

#%%
freq_tipo_vendedor.plot.bar(title="Frequência por Tipo de Vendedor", rot=0, color='green', figsize=(8,5))

#%%
freq_tipo_combustivel.plot.bar(title="Frequência por Tipo de Combustível", rot=0, color='blue', figsize=(8,5))

#%%

freq_tipo_transmissao.plot.pie(autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'], figsize=(8,8))

# Adicionar título
plt.title('Distribuição dos Tipos de Transmissão')
#frq_tipo_transmissao.plot.pie(title=)
#%%
freq_estado.plot.bar(title="Frequência por Estado do Veículo", rot=0, color='orange', figsize=(8,5))


#%%
media_preco_minimo_por_marca = carros_atualizado.groupby('marca')['preco_minimo'].mean()

# Criar gráfico de linha para a média do preço mínimo por marca
plt.figure(figsize=(12, 8))
ax = media_preco_minimo_por_marca.plot(kind='line', marker='o', color='b', linestyle='-', linewidth=2)

ax.set_title('Média do Preço Mínimo por Marca', fontsize=16)
ax.set_xlabel('Marca', fontsize=14)
ax.set_ylabel('Média do Preço Mínimo', fontsize=14)
ax.set_xticks(range(len(media_preco_minimo_por_marca.index)))  # Ajusta os ticks do eixo x
ax.set_xticklabels(media_preco_minimo_por_marca.index, rotation=45, ha='right')

# Adicionar valores no gráfico
for i, value in enumerate(media_preco_minimo_por_marca):
    ax.ylabel(i, value, f'{value:.2f}', ha='center', va='bottom')
#%%
carros_atualizado['idade_veiculo'].plot.hist(title="Distribuição da Idade do Veículo", bins=15, color='lightgreen', edgecolor='black', figsize=(10,6))

#%%
carros_atualizado['ipva'].plot.hist(title="Distribuição do IPVA", bins=15, color='lightcoral', edgecolor='black', figsize=(10,6))

#%%
carros_atualizado['transmissao_num'] = carros_atualizado['tipo_transmissao'].astype('category').cat.codes

# Calcular a correlação entre preco_venda e transmissao_num
correlacao = carros_atualizado[['preco_venda', 'transmissao_num']].corr().iloc[0, 1]
print(f'Correlação entre Preço de Venda e Tipo de Transmissão: {correlacao:.2f}')

# Criar gráfico de dispersão para visualização
plt.figure(figsize=(12, 8))
plt.scatter(x=carros_atualizado['transmissao_num'], y=carros_atualizado['preco_venda'], color='lightblue', edgecolor='black')

# Adicionar título e rótulos
plt.title('Preço de Venda em Função do Tipo de Transmissão', fontsize=16)
plt.xlabel('Tipo de Transmissão (Codificado)', fontsize=14)
plt.ylabel('Preço de Venda (R$)', fontsize=14)

# Adicionar rótulos para o eixo X
transmissao_labels = carros_atualizado['tipo_transmissao'].astype('category').cat.categories
plt.xticks(ticks=range(len(transmissao_labels)), labels=transmissao_labels, rotation=45)
plt.tight_layout()
#%%
distribuicao_potencia = carros_atualizado.groupby('marca')['potencia_maxima'].describe()
media_potencia = carros_atualizado.groupby('marca')['potencia_maxima'].mean()
media_potencia.plot(kind='bar', color='lightblue', edgecolor='black')

# Adicionar título e rótulos
plt.title('Distribuição da Potência Máxima por Marca', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Potência Máxima (hp)', fontsize=14)
#%%
correlacao = carros_atualizado.groupby('marca').apply(lambda x: x[['km_rodados', 'preco_venda']].corr().iloc[0, 1])

# Criar um gráfico de barras para a correlação
correlacao.plot(kind='bar', color='lightcoral', edgecolor='black')

# Adicionar título e rótulos
plt.title('Correlação entre KM Rodado e Preço de Venda por Marca', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Correlação', fontsize=14)
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

