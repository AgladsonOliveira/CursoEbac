import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha
df.plot(x='dia', y='venda', marker='o', linestyle='-')

# Adicionando rótulos aos eixos
plt.xlabel('Dia')
plt.ylabel('Venda')

# Adicionando título ao gráfico
plt.title('Gráfico de Venda Diária de Gasolina')

# Exibindo o gráfico
plt.show()