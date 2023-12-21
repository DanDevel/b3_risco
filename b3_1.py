import pandas as pd
import matplotlib.pyplot as plt

class Risco:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)
        self.df['Data'] = pd.to_datetime(self.df['Data'])
        self.df.set_index('Data', inplace=True)

    def visualizar_ohlc(self):
        self.df['Close'].plot(figsize=(10, 6), title='Histórico de Preços (Close)')
        plt.show()

    def calcular_retornos_diarios(self):
        self.df['Retorno Diário'] = self.df['Close'].pct_change()

    def visualizar_retornos_diarios(self):
        self.df['Retorno Diário'].plot(figsize=(10, 6), title='Retornos Diários')
        plt.show()

    def calcular_estatisticas_retornos(self):
        estatisticas_retornos = self.df['Retorno Diário'].describe()
        print("Estatísticas Descritivas dos Retornos Diários:")
        print(estatisticas_retornos)

    def calcular_volatilidade(self):
        volatilidade = self.df['Retorno Diário'].std()
        print(f'\nVolatilidade: {volatilidade}')


dados_exemplo = {
    'Data': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Open': [100, 105, 98, 102],
    'High': [110, 115, 100, 105],
    'Low': [95, 98, 94, 100],
    'Close': [105, 110, 96, 101],
}

analise_risco = Risco(dados_exemplo)
analise_risco.visualizar_ohlc()
analise_risco.calcular_retornos_diarios()
analise_risco.visualizar_retornos_diarios()
analise_risco.calcular_estatisticas_retornos()
analise_risco.calcular_volatilidade()
