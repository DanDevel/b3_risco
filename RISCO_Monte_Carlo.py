import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
media_retorno = 0.001  # Retorno médio diário
volatilidade_retorno = 0.02  # Volatilidade diária

# Configuração da simulação
dias_simulacao = 252  # Número de dias de simulação
num_simulacoes = 5  # Reduzi o número de simulações para facilitar a visualização

# Simulação de Monte Carlo
simulacoes = np.random.normal(loc=media_retorno, scale=volatilidade_retorno, size=(dias_simulacao, num_simulacoes))

# Cálculo dos retornos acumulados
retorno_acumulado = np.cumprod(1 + simulacoes, axis=0) - 1

# Visualização dos resultados com cores diferentes
plt.figure(figsize=(10, 6))

for i in range(num_simulacoes):
    plt.plot(retorno_acumulado[:, i], label=f'Simulação {i + 1}')

plt.title('Simulação de Monte Carlo - Retornos Acumulados')
plt.xlabel('Dias')
plt.ylabel('Retorno Acumulado')
plt.legend()
plt.show()
