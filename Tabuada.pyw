from tkinter import *

def tabuada(event=None):
    resultado_text.config(state=NORMAL) #verifica se a área dos resultados é editável ou não, para garantir que a próxima linha de código funcione
    resultado_text.delete(1.0, END) #caso o usuário queira ver a tabuada de outro numero, essa função apaga a tabuada anterior para deixar a tela mais limpa para a proxima tabuada
    
    try:                            #verificação se o numero que o usuario digitou é inteiro
        numero = int(entry.get())   #pega o numero digitado pelo usuario 
        for x in range(1,11):
            multiplicacao =numero * x
            resultado_text.insert(END, f"{numero} x {x} = {multiplicacao}\n")  #mostra cada multiplicação
        resultado_text.config(state=DISABLED) #faz com que o usuário não possa alterar o que é mostrado na área dos resultados
    except ValueError:
        resultado_text.insert(END, "Por favor, digite um número válido.")  #caso o usuário digite um numero invalido aparece essa msg de erro


janela = Tk()    #abre a janela da interface gráfica

janela.title("Tabuada")  #adiciona o titulo da janela

orientacaoInicial = Label(janela, text='Digite um número para calcular sua tabuada:')  #texto inicial de orientação ao usuário
orientacaoInicial.grid(column=0,row=0)  #coloca o texto de orientação na primeira linha e coluna da janela

entry = Entry(janela)   #lugar que recebe a entrada do usuário na interface gráfica
entry.grid(column=0,row=1) #posiciona a entrada na coluna 0 e na linha 1 (linha após a linha da orientação)

resultado_text = Text(janela, height = 10, width = 35) #define o local onde vão aparecer os resultados
resultado_text.grid(column=0,row=3)  #coloca esse local na coluna 0 e na linha 3 (duas linhas após a entrada do usuário)

entry.bind("<Return>", tabuada) #quando o usuário aperta a tecla enter, a função tabuada é chamada e os resultados aparecem no local definido por resultado_text

janela.mainloop() #mantém o programa rodando enquanto o usuário não fechar
