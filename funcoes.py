def ler_arquivo():
    try:
        arquivo = open("Dados de Login.txt" , "r")
    except:
        arquivo = open("Dados de Login.txt" , "w")
        arquivo.close()
        arquivo = open("Dados de Login.txt" , "r")
    dados = arquivo.readlines()
    arquivo.close()
    return dados

def salvar_arquivo(dados):
        arquivo = open("Dados de Login.txt" , "w")
        arquivo.writelines(dados)
        arquivo.close()