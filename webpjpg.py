from PIL import Image
import os

# Define a pasta com os arquivos de entrada
pasta_entrada = r"E:\Tênis\Air Jordan 1 Retro High Chicago"

# Define a pasta de saída para os arquivos JPG
pasta_saida = pasta_entrada

# Percorre todos os arquivos com a extensão .webp na pasta de entrada
for arquivo_entrada in os.listdir(pasta_entrada):
    if arquivo_entrada.endswith(".webp"):
        # Define o caminho completo para o arquivo de entrada e saída
        caminho_entrada = os.path.join(pasta_entrada, arquivo_entrada)
        caminho_saida = os.path.join(pasta_saida, os.path.splitext(arquivo_entrada)[0] + ".jpg")

        # Abre a imagem no formato WEBP e salva como JPEG
        imagem = Image.open(caminho_entrada).convert("RGB")
        imagem.save(caminho_saida, "JPEG")

        # Exibe uma mensagem de confirmação
        print(f"{arquivo_entrada} convertido para {os.path.basename(caminho_entrada)}")

        caminho = os.path.join(pasta_entrada, arquivo_entrada)
        os.remove(caminho)

        # Exibe uma mensagem de confirmação
        print(f"{arquivo_entrada} foi excluído.")