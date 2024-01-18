from tkinter import *
from tkinter import messagebox


"""def clicou() -> None:
    # como pegar o que foi digitado nos campos?
    nome = txtNome.get()
    salario = float(txtSalario.get())
    #como criar um messagebox
    messagebox.showinfo("Clicou!", f"Seu nome: {nome} \nSeu salario: {salario}")




# como criar uma janela

janela = Tk()

# como altera altura e largura da janela?
janela.geometry("400x300")
# como alterar o titulo
janela.title("Primeira janela")


# Criar um label
labelName = Label(janela, text="Nome:", font="Tahoma 16", fg="navy")
labelName.grid(row=0, column=0)

# como adicionar com pack, place ou grid
#     labelName.pack()
#     labelName.place(x=150, y=200)

txtNome = Entry(janela, font="Tahoma 16", width=22)
txtNome.grid(row=0, column=1)

labelSalario = Label(janela, text="Salario:", font="Tahoma 16", fg="navy")
labelSalario.grid(row=1, column=0)

txtSalario = Entry(janela, font="Tahoma 16", width=22)
txtSalario.grid(row=1, column=1)

# como criar um botão
btnEnviar = Button(janela, text="Enviar", font="Tahoma 16", width=10, bg="red", fg="white", command=clicou)
btnEnviar.grid(row=2, column= 1)
"""


# -----------------------------------------------




'''
def function_calcular():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    imc = peso / altura ** 2
    messagebox.showinfo(f"seu IMC é: {imc}")


janela = Tk()

janela.geometry("300x200")
janela.title("IMC")

labelPeso = Label(janela, text="peso:", font="Arial", fg="grey")
labelPeso.grid(row=0, column=0)
txtPeso = Entry(janela, font='Roboto', width=20)
txtPeso.grid(row=0, column=1)

labelAltura = Label(janela, text="altura:", font="Arial", fg="grey")
labelAltura.grid(row=1, column=0)
txtAltura = Entry(janela, font="Roboto", width=20,)
txtAltura.grid(row=1, column=1)

bt = Button(janela, text="Calcular", font="Roboto", bg="blue", fg="white", width=15, command=function_calcular)
bt.grid(row=2, column=1)


# como rodar o programa no S.O.
janela.mainloop()
'''
def function_Limpar() -> None:
    display.delete(0, END)

def function_inserir(valor: str) -> None:
    display.insert(END, valor)

def function_calcularResultado() -> None:
    textoDisplay = display.get()
    resultado = eval(textoDisplay)
    function_Limpar()
    function_inserir(resultado)





janela = Tk()
janela.title("Calculadora")
display = Entry(janela, bg="black", font="Tahoma 23", width=20, fg="white")
display.pack()

frame = Frame(janela)
frame.pack()

gray = "#333333"
orange = "#ff9500"

# botoes
btn0 = Button(frame, text="0", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("0"))
btn1 = Button(frame, text="1", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("1"))
btn2 = Button(frame, text="2", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("2"))
btn3 = Button(frame, text="3", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("3"))
btn4 = Button(frame, text="4", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("4"))
btn5 = Button(frame, text="5", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("5"))
btn6 = Button(frame, text="6", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("6"))
btn7 = Button(frame, text="7", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("7"))
btn8 = Button(frame, text="8", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("8"))
btn9 = Button(frame, text="9", bg=gray, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("9"))
btnSomar = Button(frame, text="+", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("+"))
btnSubtrair = Button(frame, text="-", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("-"))
btnMultiplicar = Button(frame, text="*", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("*"))
btnDividir = Button(frame, text="/", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("/"))
btnLimpar = Button(frame, text="c", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6, command=function_Limpar)
btnPonto = Button(frame, text=".", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command=lambda: function_inserir("."))
btnIgual = Button(frame, text="=", bg=orange, fg="white", font="Tahoma 16 bold", height=3, width=6,command= function_calcularResultado)


#Primeira linha
btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btnSomar.grid(row=0, column=3)

#Segunda linha
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btnSubtrair.grid(row=1, column=3)

#terceira linha
btn3.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn1.grid(row=2, column=2)
btnMultiplicar.grid(row=2, column=3)

#quarta linha
btnIgual.grid(row=3, column=0)
btn0.grid(row=3, column=1)
btnLimpar.grid(row=3, column=2)
btnDividir.grid(row=3, column=3)






janela.mainloop()