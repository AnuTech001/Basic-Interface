# Universal
from universal import *

# Funções de criação dos objetos
lista = []

def cadastro_animal():
    nome = entry_nome.get()
    idade = entry_idade.get()
    tipo = var_tipo.get()
    porte = entry_porte.get()
    raca = entry_raca.get()
    erro = 0

    if tipo == 'Cachorro':
        if nome == '':  # Nome
            messagebox.showinfo("Erro!", "O parâmetro 'Nome' deve ser preenchido")   # Mensagem de erro
            erro = 1

        elif idade == '':   # Idade
            messagebox.showinfo("Erro!", "O parâmetro 'Idade' deve ser preenchido")   # Mensagem de erro
            erro = 1

        elif porte == '':   # Porte
            messagebox.showinfo("Erro!", "O parâmetro 'Porte' deve ser preenchido")   # Mensagem de erro
            erro = 1

        elif raca == '':    # Raça
            messagebox.showinfo("Erro!", "O parâmetro 'Raça' deve ser preenchido")   # Mensagem de erro
            erro = 1
        
        if erro == 1:   # Retorna a função em caso de erro
            return
        
        c = Cachorro(nome, idade, porte, raca)
        salvar(c)
        messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")  # Mensagem de cadastro

    elif tipo == 'Gato':
        if nome == '':  # Nome
            messagebox.showinfo("Erro!", "O parâmetro 'Nome' deve ser preenchido")   # Mensagem de erro
            erro = 1

        elif idade == '':   # Idade
            messagebox.showinfo("Erro!", "O parâmetro 'Idade' deve ser preenchido")   # Mensagem de erro
            erro = 1

        elif raca == '':    # Raça
            messagebox.showinfo("Erro!", "O parâmetro 'Raça' deve ser preenchido")   # Mensagem de erro
            erro = 1

        if erro == 1:   # Retorna a função em caso de erro
            return

        g = Gato(nome, idade, raca)
        salvar(g)
        messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")  # Mensagem de cadastro

def salvar(objeto):
    for item in lista:
        if item.mostrar() == objeto.mostrar():
            messagebox.showinfo("Erro!", "Este item já foi cadastrado")
            return
    lista.append(objeto)
    atualiza_lista_box()

def atualiza_lista_box():
    listbox.delete(0, tk.END)
    for objeto in lista:
        listbox.insert(tk.END, objeto.mostrar())

# Configuração da Janela
janela = tk.Tk()
janela.title("Cadastro de Veículos")
janela.geometry("1500x500")

janela.grid_rowconfigure(0, weight = 1)
janela.grid_columnconfigure(0, weight = 1)

# Configuração das abas
janelinha = ttk.Notebook(janela)
janelinha.grid(row = 0, column = 0, sticky = 'nsew')

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight = 1)
tab1.grid_columnconfigure(0, weight = 1)
tab1.grid_columnconfigure(1, weight = 1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight = 1)
tab2.grid_columnconfigure(0, weight = 1)

janelinha.add(tab1, text = "Cadastro")
janelinha.add(tab2, text = "lista")

# Mensagens a serem escritas
label1 = tk.Label(tab1, text = "Nome:", font = ("", 15))   # Nome
label1.grid(row = 0, column = 0, sticky = 'w', padx = 10)

entry_nome = tk.Entry(tab1, font = ("", 15))
entry_nome.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 5)

#-------------------------------------------------------------------------------

label2 = tk.Label(tab1, text = "Idade:", font = ("", 15))  # Idade
label2.grid(row = 1, column = 0, sticky = 'w', padx = 10)

entry_idade = tk.Entry(tab1, font = ("", 15))
entry_idade.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 5)

#-------------------------------------------------------------------------------

label3 = tk.Label(tab1, text = "Porte (apenas para cães):", font = ("", 15)) # Porte (em caso de cães)
label3.grid(row = 2, column = 0, sticky = 'w', padx = 10)

entry_porte = tk.Entry(tab1, font = ("", 15))
entry_porte.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 5)

#-------------------------------------------------------------------------------

label4 = tk.Label(tab1, text = "Raça:", font = ("", 15)) # Raça
label4.grid(row = 3, column = 0, sticky = 'w', padx = 10)

entry_raca = tk.Entry(tab1, font = ("", 15))
entry_raca.grid(row = 3, column = 1, sticky = 'nsew', padx = 10, pady = 5)

#-------------------------------------------------------------------------------

# Mais configurações de interface
tk.Label(tab1, text = "Tipo", font = ("", 15)).grid(row = 4, column = 0, sticky = 'w', padx = 10)
var_tipo = tk.StringVar(value = "Cachorro")
tk.Radiobutton(tab1, text = "Cachorro", font = ("", 15), variable = var_tipo, value = "Cachorro").grid(row = 4, column = 1, sticky = 'w', padx = 10)
tk.Radiobutton(tab1, text = "Gato", font = ("", 15), variable = var_tipo, value = "Gato").grid(row = 4, column = 1, sticky = 'e', padx = 10)

tk.Button(tab1, text = "Cadastrar", font = ("", 15), command = cadastro_animal).grid(row = 5, column = 1, sticky = 'nsew', padx = 10)

#-------------------------------------------------------------------------------    tab 2

listbox = tk.Listbox(tab2)
listbox.config(font = ("", 15))
listbox.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
tk.Button(tab2, text = "Atualizar", font = ("", 15), command = atualiza_lista_box).grid(row = 1, column = 0)

janela.mainloop()