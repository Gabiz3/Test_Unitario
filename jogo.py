import tkinter as tk
from tkinter import messagebox


def calcular_numeros(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero!")
        return num1 / num2
    else:
        raise ValueError("Operação inválida")


""""
def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacao = operacao_var.get()

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero!")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Erro", "Operação inválida")
            return

        resultado_var.set(f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Entradas
tk.Label(janela, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1, padx=5, pady=5)

# Operações
tk.Label(janela, text="Operação:").grid(row=2, column=0, padx=5, pady=5)
operacao_var = tk.StringVar(janela)
operacao_var.set('+')  # valor padrão
operacoes_menu = tk.OptionMenu(janela, operacao_var, '+', '-', '*', '/')
operacoes_menu.grid(row=2, column=1, padx=5, pady=5)

# Botão calcular
tk.Button(janela, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(janela, textvariable=resultado_var, font=("Arial", 12))
resultado_label.grid(row=4, column=0, columnspan=2, pady=5)

# Inicia a aplicação
janela.mainloop()
"""