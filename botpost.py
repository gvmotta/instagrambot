from instagrapi import Client
from instagrapi.types import Usertag, Location
from pyChatGPT import ChatGPT
import os

nome = str(input("Digite o nome do tênis: "))

with open(r'C:\Users\gusta\OneDrive\Área de Trabalho\sessaodochatgpt.txt', 'r') as arquivo:
    sessaogpt = arquivo.read()
    arquivo.close()


api = ChatGPT(sessaogpt)

resp = api.send_message('Seja um ótimo vendedor e faça uma descrição que me convença a comprar o tênis {} começando a frase falando "O tênis" em um texto de um parágrafo de 3 linhas sem falar da sua sola de EVA'.format(nome))
api.reset_conversation()  # reset the conversation
# Encontra o índice da primeira ocorrência da palavra "tênis"
indice = resp['message'].find('O tênis')

# Faz slicing da string a partir do índice encontrado
parte_tenis = resp['message'][indice:].rstrip()

hashtags = "\n\n#sneakers #dunk #nike #airjordan #store #tenis"

resp1 = "{}\n- Fotos Reais do produto\n- Chama direct para mais detalhes\n\n".format(nome) + parte_tenis + hashtags

print(resp1)

nome_insta = os.environ.get('username_insta')
senha_insta = os.environ.get('senha_insta')

cl = Client()
cl.login(nome_insta, senha_insta)

List = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\1.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\2.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\3.jpg"]
List2 = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\4.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\5.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\6.jpg"]
List3 = [r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\7.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\8.jpg", r"C:\Users\gusta\OneDrive\Imagens\app\fotosparapostar\9.jpg"]

media = cl.album_upload(
    paths=List3,
    caption=resp1,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 0,
    }
)
media = cl.album_upload(
    paths=List2,
    caption=resp1,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 0,
    }
)

media = cl.album_upload(
    paths=List,
    caption=resp1,
    extra_data={
        "custom_accessibility_caption": "",
        "like_and_view_counts_disabled": 0,
    }
)