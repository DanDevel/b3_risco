import pandas as pd
import matplotlib.pyplot as plt

# Suponhamos que você tenha um DataFrame com dados OHLC para clubes e fundos
# Vou criar um exemplo fictício para ilustrar

dados = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Open': [100, 105, 98, 102],
    'High': [110, 115, 100, 105],
    'Low': [95, 98, 94, 100],
    'Close': [105, 110, 96, 101],
}

df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])
df.set_index('Data', inplace=True)

# Visualizar os dados OHLC
df['Close'].plot(figsize=(10, 6), title='Histórico de Preços (Close)')
plt.show()

# Calcular Retornos Diários
df['Retorno Diário'] = df['Close'].pct_change()

# Visualizar os retornos diários
df['Retorno Diário'].plot(figsize=(10, 6), title='Retornos Diários')
plt.show()

# Calcular Estatísticas Descritivas dos Retornos
estatisticas_retornos = df['Retorno Diário'].describe()
print("Estatísticas Descritivas dos Retornos Diários:")
print("Retornos Diários: ", estatisticas_retornos)

# Calcular Volatilidade
volatilidade = df['Retorno Diário'].std()
print(f'\nVolatilidade: {volatilidade}')
