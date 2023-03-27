from instagrapi import Client
from PIL import Image
import shutil, random, os
from datetime import datetime

caminho_origem = r'C:\Users\gusta\OneDrive\Imagens\app\fotosenvios'
caminho_destino = r'C:\Users\gusta\OneDrive\Imagens\app\3img'

arquivos = os.listdir(caminho_origem)
arquivos_aleatorios = random.sample(arquivos, 3)

for arquivo in arquivos_aleatorios:
    caminho_arquivo = os.path.join(caminho_origem, arquivo)
    shutil.move(caminho_arquivo, caminho_destino)


arquivos = os.listdir(caminho_destino)
arquivos_aleatorios = random.sample(arquivos, 3)

for i, nome_atual in enumerate(arquivos_aleatorios):
    i+=1
    if i == 1:
        nome_novo = f"image.jpg"
    if i == 2:
        nome_novo = f"image2.jpg"
    if i ==3:
        nome_novo = f"image3.jpg"
    caminho_atual = os.path.join(caminho_destino, nome_atual)
    caminho_novo = os.path.join(caminho_destino, nome_novo)
    os.rename(caminho_atual, caminho_novo)

# abrir a imagem que você deseja cortar
img = Image.open(r'C:\Users\gusta\OneDrive\Imagens\app\3img\image.jpg')
img2 = Image.open(r'C:\Users\gusta\OneDrive\Imagens\app\3img\image2.jpg')
img3 = Image.open(r'C:\Users\gusta\OneDrive\Imagens\app\3img\image3.jpg')
img4= Image.open(r'C:\Users\gusta\OneDrive\Imagens\app\plane.png')
img4 = img4.convert("RGBA")

# obter as dimensões da imagem
largura, altura = img.size

# calcular as coordenadas de início e fim para cortar a imagem no centro
esquerda = (largura - 1080) / 2
topo = (altura - 640) / 2
direita = (largura + 1080) / 2
inferior = (altura + 640) / 2

# cortar a imagem no centro
img_cortada = img.crop((esquerda, topo, direita, inferior))
img2_cortada = img2.crop((esquerda, topo, direita, inferior))
img3_cortada = img3.crop((esquerda, topo, direita, inferior))

# salvar a imagem cortada
img_cortada.save(r'C:\Users\gusta\OneDrive\Imagens\app\cortada\imagem_cortada.jpg')
img2_cortada.save(r'C:\Users\gusta\OneDrive\Imagens\app\cortada\imagem2_cortada.jpg')
img3_cortada.save(r'C:\Users\gusta\OneDrive\Imagens\app\cortada\imagem3_cortada.jpg')

# redimensionar as imagens para 1080 x 640 pixels
largura1 = 1080
altura1 = 640

img_cortada = img_cortada.resize((largura, altura))
img2_cortada = img2_cortada.resize((largura, altura))
img3_cortada = img3_cortada.resize((largura, altura))


# criar uma nova imagem com as dimensões desejadas
imagem_final = Image.new('RGB', (largura, altura*3), (255, 255, 255, 0))   

# colar as imagens na nova imagem
imagem_final.paste(img_cortada, (0, 0))
imagem_final.paste(img2_cortada, (0, altura))
imagem_final.paste(img3_cortada, (0, altura*2))



# redimensionar a imagem final para 1080 x 1920 pixels
largura_final = 1080
altura_final = 1920

imagem_final = imagem_final.resize((largura_final, altura_final))
# salvar a imagem final
imagem_final.save(r'C:\Users\gusta\OneDrive\Imagens\app\imagem_stories.jpg')

img_jpg = Image.open(r"C:\Users\gusta\OneDrive\Imagens\app\imagem_stories.jpg")  
width, height = img_jpg.size
x = int((width - img4.width) / 2)
y = int((height - img4.height) / 2) + 250

# Cria uma nova imagem com o fundo da imagem JPG
nova_imagem = Image.new("RGB", (width, height), (255, 255, 255))
nova_imagem.paste(img_jpg, (0, 0))

# Cole a imagem com fundo transparente no centro da nova imagem
nova_imagem.paste(img4, (x, y), img4)

nova_imagem.save(r"C:\Users\gusta\OneDrive\Imagens\app\result\imgstories.jpg")


cl = Client()
cl.login("splashsneakers.inc", "LUCIANe101@#")

cl.photo_upload_to_story(path=r'C:\Users\gusta\OneDrive\Imagens\app\result\imgstories.jpg')


# Especifique o caminho atual do arquivo JPEG
caminho_origem = r'C:\Users\gusta\OneDrive\Imagens\app\3img'
caminho_destino = r'C:\Users\gusta\OneDrive\Imagens\app\fotosenvios!'

arquivos = os.listdir(caminho_origem)
arquivos_aleatorios = random.sample(arquivos, 3)

now = datetime.now() # current date and time
date_time = now.strftime("%m-%d-%Y-%H-%M-%S")


for i, nome_atual in enumerate(arquivos_aleatorios):
    nome_novo = f"1.{date_time}{i}.jpg"
    caminho_atual = os.path.join(caminho_origem, nome_atual)
    caminho_novo = os.path.join(caminho_origem, nome_novo)
    os.rename(caminho_atual, caminho_novo)

arquivos = os.listdir(caminho_origem)
arquivos_aleatorios = random.sample(arquivos, 3)

# Para cada arquivo escolhido aleatoriamente, mova-o para a pasta de destino
for arquivo in arquivos_aleatorios:
    caminho_arquivo = os.path.join(caminho_origem, arquivo)
    shutil.move(caminho_arquivo, caminho_destino)