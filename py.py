import tkinter as tk
import pandas as pd

# Função que realiza a análise dos dados
def analisar_jogo():
    # Dados fictícios para exemplificação
    data = {
        'Jogo': [' sao paulo vs botafogo', 'santos vs vila nova'],
        'Cartões': [5, 3],
        'Gols': [2, 1],
        'Escanteios': [7, 4],
        'Vitória Provável': [' sao paulo', 'santos']
    }
    df = pd.DataFrame(data)
    
    # Exibir os resultados na interface gráfica
    resultado_texto = ""
    for i, row in df.iterrows():
        resultado_texto += f"Jogo: {row['Jogo']}\n"
        resultado_texto += f"Cartões: {row['Cartões']}\n"
        resultado_texto += f"Gols: {row['Gols']}\n"
        resultado_texto += f"Escanteios: {row['Escanteios']}\n"
        resultado_texto += f"Vitória Provável: {row['Vitória Provável']}\n"
        resultado_texto += "-----------------------------\n"
    
    resultado_label.config(text=resultado_texto)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Análise de Apostas - Série A")

# Botão para realizar a análise
analisar_button = tk.Button(root, text="Analisar Jogos", command=analisar_jogo)
analisar_button.pack()

# Label para exibir os resultados
resultado_label = tk.Label(root, text="", justify=tk.LEFT)
resultado_label.pack()

# Loop da interface gráfica
root.mainloop()
