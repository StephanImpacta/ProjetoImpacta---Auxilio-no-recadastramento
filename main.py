import tkinter as tk;#Interface gráfica
import sqlite3;#Integração com o SQlite
import pandas as pd; #Exportar para Excel



conect=sqlite3.connect('armas.db')#Cria conexão com o sql

c=conect.cursor()#Execução da conexão

#Cria tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS armas(
 NumeroSerie INTEGER PRIMARY KEY,
 NúmeroSigma INTERGER NOT NULL, 
 DataCRAF TEXT NOT NULL,
 ValidadeCRAF TEXT NOT NULL,
 Marca TEXT,
 Modelo TEXT,
 Tipo TEXT,
 Calibre TEXT,
 País TEXT,
 Alma TEXT,
 NúmeroRaias INTEGER,
 SentidoRaias TEXT,
 Capacidade INTEGER,
 NúmeroCanos INTEGER,
 ComprimentoCano INTEGER,
 Funcionamento TEXT,
 Acabamento TEXT,
 Restrita TEXT
 )''')

conect.commit()#Commita a operação anterior
conect.close()#Encerra a conexão

#Função botão
def cadastrar_arma():
    conectBotao=sqlite3.connect('armas.db')#Cria conexão com o sql

    c1=conectBotao.cursor()

    #Inserir os valores na tabela
    c1.execute( "INSERT INTO armas VALUES(:nserie, :nsigma, :dcraf, :vcraf, :marca, :modelo, :tipo, :calibre, :pais, :alma, :nraias, :sraias, :capacidade, :ncanos, :comprimento, :func,:acabamento, :restrito)",{
        'nserie':entry_NumeroSerie.get(),
        'nsigma':entry_NumeroSigma.get(),
        'dcraf':entry_DataCRAF.get(),
        'vcraf':entry_ValCRAF.get(),
        'marca':entry_Marca.get(),
        'modelo':entry_Modelo.get(),
        'tipo':entry_Tipo.get(),
        'calibre':entry_Calibre.get(),
        'pais':entry_Pais.get(),
        'alma':entry_Alma.get(),
        'nraias':entry_Raias.get(),
        'sraias':entry_SRaias.get(),
        'capacidade':entry_Cap.get(),
        'ncanos':entry_NCanos.get(),
        'comprimento':entry_Comp.get(),
        'func':entry_Func.get(),
        'acabamento':entry_Acab.get(),
        'restrito':entry_Restr.get()



    }
    )       
    conectBotao.commit()
    conectBotao.close()

#limpar as caixas de texto depois do cadastro
    entry_NumeroSerie.delete(0,"end")
    entry_NumeroSigma.delete(0,"end")
    entry_DataCRAF.delete(0,"end")
    entry_ValCRAF.delete(0,"end")
    entry_Marca.delete(0,"end")
    entry_Modelo.delete(0,"end")
    entry_Tipo.delete(0,"end")
    entry_Calibre.delete(0,"end")
    entry_Pais.delete(0,"end")
    entry_Alma.delete(0,"end")
    entry_Raias.delete(0,"end")
    entry_SRaias.delete(0,"end")
    entry_Cap.delete(0,"end")
    entry_NCanos.delete(0,"end")
    entry_Comp.delete(0,"end")
    entry_Func.delete(0,"end")
    entry_Acab.delete(0,"end")
    entry_Restr.delete(0,"end")




def listar_arma():
            conectListar=sqlite3.connect('armas.db')#Cria conexão com o sql

            c2=conectListar.cursor()

    #Inserir os valores na tabela
            c2.execute( 'SELECT * FROM armas')
            armas_cadastradas=c2.fetchall()
            dicionario={}
            for i in armas_cadastradas:
                    c=0
                    dicionario[c]=i
                    c+=1
                    

            label_texto=tk.Label(janela, text=dicionario[i])
            label_texto.grid(column= 2, row=2, rowspan=10, columnspan=3, ipadx=200)

        
            conectListar.commit()
            conectListar.close()



janela=tk.Tk()#Inicio do controle da interface gráfica

janela.title('Ferramenta de Recadastramento de Armas')#Título exibido na interface gráfica

#Título da caixa de texto

label_Serie=tk.Label(janela, text="Número de Série")
label_Serie.grid(row=1, column=0, padx=10, pady=10)

label_NumeroSigma=tk.Label(janela, text="Número Sigma")
label_NumeroSigma.grid(row=2, column=0, padx=10, pady=10)

label_DataCRAF=tk.Label(janela, text="Data de emissão do CRAF")
label_DataCRAF.grid(row=3, column=0, padx=10, pady=10)

label_ValCRAF=tk.Label(janela, text="Data de Validade do CRAF")
label_ValCRAF.grid(row=4, column=0, padx=10, pady=10)

label_Marca=tk.Label(janela, text="Marca da arma")
label_Marca.grid(row=5, column=0, padx=10, pady=10)

label_Modelo=tk.Label(janela, text="Modelo da arma")
label_Modelo.grid(row=6, column=0, padx=10, pady=10)

label_Tipo=tk.Label(janela, text="Tipo da arma")
label_Tipo.grid(row=7, column=0, padx=10, pady=10)

label_Calibre=tk.Label(janela, text="Calibre da arma")
label_Calibre.grid(row=8, column=0, padx=10, pady=10)

label_Pais=tk.Label(janela, text="País de Fabricação da arma")
label_Pais.grid(row=9, column=0, padx=10, pady=10)

label_Alma=tk.Label(janela, text="Alma do cano")
label_Alma.grid(row=10, column=0, padx=10, pady=10)

label_Raias=tk.Label(janela, text="Número de Raias do cano")
label_Raias.grid(row=11, column=0, padx=10, pady=10)

label_SRaias=tk.Label(janela, text="Sentido das Raias")
label_SRaias.grid(row=12, column=0, padx=10, pady=10)

label_Cap=tk.Label(janela, text="Capacidade de Munição")
label_Cap.grid(row=13, column=0, padx=10, pady=10)

label_NCanos=tk.Label(janela, text="Número de Canos")
label_NCanos.grid(row=14, column=0, padx=10, pady=10)

label_Comp=tk.Label(janela, text="Comprimento do Cano")
label_Comp.grid(row=15, column=0, padx=10, pady=10)

label_Func=tk.Label(janela, text="Tipo de Funcionamento")
label_Func.grid(row=16, column=0, padx=10, pady=10)

label_Acab=tk.Label(janela, text="Tipo de Acabamento")
label_Acab.grid(row=17, column=0, padx=10, pady=10)

label_Restr=tk.Label(janela, text="Calibre Restrito? (s/n)")
label_Restr.grid(row=18, column=0, padx=10, pady=10)

#Caixas de Texto

label_texto=tk.Label(janela, text="Resultado:")
label_texto.grid(column= 2, row=2, rowspan=10, columnspan=3, ipadx=200)


entry_NumeroSerie=tk.Entry(janela, text="Número de Série")
entry_NumeroSerie.grid(row=1, column=1, padx=10, pady=10)

entry_NumeroSigma=tk.Entry(janela, text="Número Sigma")
entry_NumeroSigma.grid(row=2, column=1, padx=10, pady=10)

entry_DataCRAF=tk.Entry(janela, text="Data de emissão do CRAF")
entry_DataCRAF.grid(row=3, column=1, padx=10, pady=10)

entry_ValCRAF=tk.Entry(janela, text="Data de Validade do CRAF")
entry_ValCRAF.grid(row=4, column=1, padx=10, pady=10)

entry_Marca=tk.Entry(janela, text="Marca da arma")
entry_Marca.grid(row=5, column=1, padx=10, pady=10)

entry_Modelo=tk.Entry(janela, text="Modelo da arma")
entry_Modelo.grid(row=6, column=1, padx=10, pady=10)

entry_Tipo=tk.Entry(janela, text="Tipo da arma")
entry_Tipo.grid(row=7, column=1, padx=10, pady=10)

entry_Calibre=tk.Entry(janela, text="Calibre da arma")
entry_Calibre.grid(row=8, column=1, padx=10, pady=10)

entry_Pais=tk.Entry(janela, text="País de Fabricação da arma")
entry_Pais.grid(row=9, column=1, padx=10, pady=10)

entry_Alma=tk.Entry(janela, text="Alma do cano")
entry_Alma.grid(row=10, column=1, padx=10, pady=10)

entry_Raias=tk.Entry(janela, text="Número de Raias do cano")
entry_Raias.grid(row=11, column=1, padx=10, pady=10)

entry_SRaias=tk.Entry(janela, text="Sentido das Raias")
entry_SRaias.grid(row=12, column=1, padx=10, pady=10)

entry_Cap=tk.Entry(janela, text="Capacidade de Munição")
entry_Cap.grid(row=13, column=1, padx=10, pady=10)

entry_NCanos=tk.Entry(janela, text="Número de Canos")
entry_NCanos.grid(row=14, column=1, padx=10, pady=10)

entry_Comp=tk.Entry(janela, text="Comprimento do Cano")
entry_Comp.grid(row=15, column=1, padx=10, pady=10)

entry_Func=tk.Entry(janela, text="Tipo de Funcionamento")
entry_Func.grid(row=16, column=1, padx=10, pady=10)

entry_Acab=tk.Entry(janela, text="Tipo de Acabamento")
entry_Acab.grid(row=17, column=1, padx=10, pady=10)

entry_Restr=tk.Entry(janela, text="Calibre Restrito? (s/n)")
entry_Restr.grid(row=18, column=1, padx=10, pady=10)

#Botões

botao_cadastrar=tk.Button(janela, text="Cadastrar Arma", command=cadastrar_arma)
botao_cadastrar.grid(row=22, column=0, padx=10, pady=10, ipadx=200, columnspan=2)

botao_listar=tk.Button(janela, text="Listar Armas Cadastradas", command=listar_arma)
botao_listar.grid(row=22, column=0, padx=10, pady=10, ipadx=200, columnspan=2)


janela.mainloop()