import os
import shutil

# Define a pasta de origem e destino
pasta_origem = r"E:\Tênis\Air Jordan 1 Low Travis Scott Black Phantom"
pasta_destino = r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar"

# Lista todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

# Exibe uma lista numerada de todos os arquivos
for i, arquivo in enumerate(arquivos):
    print(f"{i}: {arquivo}")
indice_arquivo = 0
while(indice_arquivo != -1):
    # Pergunta ao usuário qual arquivo ele deseja mover
    indice_arquivo = str(input("Digite o caminho do arquivo que deseja mover: "))
    if(indice_arquivo== -1):
        raise Exception("Program terminated")

    # Obtém o nome do arquivo selecionado
    arquivo_selecionado = arquivos[indice_arquivo]

    # Pede um novo nome para o arquivo
    novo_nome = input("Digite o novo nome do arquivo: ")

    # Define o caminho completo para o arquivo de origem e destino
    caminho_origem = os.path.join(pasta_origem, arquivo_selecionado)
    caminho_destino = os.path.join(pasta_destino, novo_nome+ ".jpg")

    # Move o arquivo para a pasta de destino com o novo nome
    shutil.copy(caminho_origem, caminho_destino)

    # Exibe uma mensagem de confirmação
    print(f"O arquivo {arquivo_selecionado} foi movido para {novo_nome}.jpg")