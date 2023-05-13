import tkinter as tk;#Interface gráfica
import sqlite3;#Integração com o SQlite
import pandas as pd; #Exportar para Excel
from tkinter import Listbox;




#================================FUNÇÕES=====================================================

#Função para criar a Tabela
def gerar_tabela():

    conect=sqlite3.connect('armas.db')#Cria conexão com o sql

    c=conect.cursor()#Execução da conexão

   
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
    )''') #Cria tabela se não existir

    conect.commit()#Commita a operação anterior
    conect.close()#Encerra a conexão




#Função botão gerar banco de dados
def cadastrar_arma():

    conectBotao=sqlite3.connect('armas.db')#Cria conexão com o sql

    c1=conectBotao.cursor()#Cria o mensageiro

    
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
        'restrito':entry_Restr.get()#Inserir os valores na tabela



    }
    )     
   
    conectBotao.commit()#Confirma as ações realizadas
    conectBotao.close()#Encerra a conexão

    label_Texto=tk.Label(janela, text=f"{entry_Modelo.get()} cadastrado com sucesso!")
    label_Texto.grid(row=4, column=2, padx=10, pady=10, ipadx=200, columnspan=1, rowspan=18)#Informa que o produto foi cadastrado com sucesso



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
    entry_Restr.delete(0,"end")#limpar as caixas de texto depois do cadastro


#Função para exportar tabela para o excel

def export_database():
     conectBanco=sqlite3.connect('armas.db')#Cria Conexão cCom o Banco de Dados
     
     c2=conectBanco.cursor()#Cria um mensageiro 
     c2.execute('SELECT *, oid FROM armas')#Seleciona todos os itens cadastrados na tabela
     armasCadastradas=c2.fetchall()#Armazena as informações recuperadas da tabela
     armasCadastradas=pd.DataFrame(armasCadastradas, columns=['Número de Série','Número Sigma','Data de Emissão do CRAF','Validade do CRAF', 'Marca', 'Modelo','Tipo', 'Calibre','País','Alma','Número de Raias','Sentido das Raias', 'Capacidade', 'Número de Canos', 'Comprimento do Cano', 'Funcionamento','Acabamento','É restrita?', 'id_banco'])#Cria as colunas da tabela
     armasCadastradas.to_excel('ArmasCadastradas.xlsx') #Cria o arquivo excel e exporta os dados para a tabela

     label_Texto=tk.Label(janela, text=f"Documento exportado com Sucesso!")
     label_Texto.grid(row=4, column=2, padx=10, pady=10, ipadx=200, columnspan=2, rowspan=18) #Muda a informação da Label para indicar que o documento foi exportado com sucesso



     conectBanco.commit()#Confirma as ações
     conectBanco.close()#Encerra a conexão



#Função para contar as armas cadastradas, eindicando a quantidade de armas de calibre restrito e de calibre permitido
def lista_armas():
    conectlista=sqlite3.connect('armas.db')
    c3=conectlista.cursor()
    c3.execute("SELECT*, oid FROM armas WHERE restrita='s'")
    armasRestritas=c3.fetchall()
    restritas=len(armasRestritas)


    c4=conectlista.cursor()
    c4.execute("SELECT*, oid FROM armas WHERE restrita='n'")
    armasPermitidas=c4.fetchall()
    permitidas=len(armasPermitidas)

    total=(permitidas+restritas)

    conectlista.commit()#Confirma as ações
    conectlista.close()#Encerra a conexão


    label_Texto=tk.Label(janela, text=f"{total} ARMAS FORAM CADASTRADAS:  \n \n-{restritas} armas de calibre RESTRITO e \n- {permitidas} armas de calibre PERMITIDO")
    label_Texto.grid(row=4, column=2, padx=10, pady=10, ipadx=200, columnspan=2, rowspan=18) #Muda a informação da Label para indicar a quantidade de armas cadastradas e de quais calibres.

#Função para apagar o banco de dados 
def apaga_banco():
    conectapaga=sqlite3.connect('armas.db')
    c5=conectapaga.cursor()
    c5.execute('DROP TABLE armas')

  


    label_Texto=tk.Label(janela, text="O banco de dados foi excluido com sucesso")
    label_Texto.grid(row=4, column=2, padx=10, pady=10, ipadx=200, columnspan=2, rowspan=18) #Muda a informação da Label para indicar que a vase de dados foi excluida com sucesso


    conectapaga.commit()#Confirma as ações
    conectapaga.close()#Encerra a conexão



#=========================INICIO DA INTERFACE GRÁFICA=======================================
janela=tk.Tk()

janela.title('Ferramenta de Recadastramento de Armas')#Título exibido na interface gráfica

#=========================TÍTULO DAS CAIXAS DE TEXTO========================================

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


#=============================CAIXAS DE TEXTO===============================================


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

#=================================BOTÕES====================================================

botao_gerarTabela=tk.Button(janela, text="Gerar Banco de Dados", command=gerar_tabela)
botao_gerarTabela.grid(row=1, column=2, padx=10, pady=10, ipadx=200, columnspan=2)
#Botão para gerar Banco de Dados


botao_cadastrar=tk.Button(janela, text="Cadastrar Arma", command=cadastrar_arma)
botao_cadastrar.grid(row=2, column=2, padx=10, pady=10, ipadx=200, columnspan=2)
#Botão para Cadastrar arma no banco de dados


botao_exibir=tk.Button(janela, text="Exportar tabela para excel", command=export_database)
botao_exibir.grid(row=3, column=2, padx=10, pady=10, ipadx=200, columnspan=2)
#Botão para Exportar tabela para o Excel

botao_listar=tk.Button(janela, text="Listar Armas Cadastradas", command=lista_armas)
botao_listar.grid(row=4,column=2, padx=10, pady=10, ipadx=200, columnspan=2) 
#Botão para lostar as armas cadastradas

botao_apagar=tk.Button(janela, text="Apagar Banco de Dados", command=apaga_banco)
botao_apagar.grid(row=5,column=2, padx=10, pady=10, ipadx=200, columnspan=2) 
#Botão para apagar o banco de dados


janela.mainloop()
