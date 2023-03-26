from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from PIL import Image, ImageDraw, ImageFont
import imageio

# abrir a imagem que você deseja cortar
img = Image.open('app/image.jpg')
img2 = Image.open('app/image2.jpg')
img3 = Image.open('app/image3.jpg')

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
img_cortada.save('app/imagem_cortada.jpg')
img2_cortada.save('app/imagem2_cortada.jpg')
img3_cortada.save('app/imagem3_cortada.jpg')

# redimensionar as imagens para 1080 x 640 pixels
largura1 = 1080
altura1 = 640

img_cortada = img.resize((largura, altura))
img2_cortada = img2.resize((largura, altura))
img3_cortada = img3.resize((largura, altura))

# criar uma nova imagem com as dimensões desejadas
imagem_final = Image.new('RGB', (largura, altura*3))

# colar as imagens na nova imagem
imagem_final.paste(img, (0, 0))
imagem_final.paste(img2, (0, altura))
imagem_final.paste(img3, (0, altura*2))

# redimensionar a imagem final para 1080 x 1920 pixels
largura_final = 1080
altura_final = 1920

imagem_final = imagem_final.resize((largura_final, altura_final))

# salvar a imagem final
imagem_final.save('app/imagem_stories.jpg')

# Defina a duração de cada frame em segundos
duration = 0.5

# Abra a imagem que você deseja adicionar o texto
img = Image.open("imagem.jpg")

# Crie um objeto ImageDraw para desenhar na imagem
draw = ImageDraw.Draw(img)

# Defina a fonte que você deseja usar
font = ImageFont.truetype("Caminho/Para/A/Fonte.ttf", 50)

# Crie uma lista vazia para armazenar os frames da animação
frames = []

# Crie um loop para criar cada frame da animação
for i in range(10):
    # Copie a imagem original para um novo objeto Image
    frame = img.copy()

    # Escreva o texto na imagem
    draw = ImageDraw.Draw(frame)
    draw.text((100, 100), "Envios de hoje ✈️", font=font)

    # Adicione o frame à lista de frames
    frames.append(frame)

# Salve a animação em formato MP4
output_file = "animacao.mp4"
imageio.mimsave(output_file, frames, format='FFMPEG', fps=1/duration)


cl = Client()
cl.login("botpythonezica", "luciane101")

profile_name = cl.user_info_by_username('splashsneakers.inc')

cl.photo_upload_to_story(
    path='app/imagem_stories.jpg', 
    caption="Envios de hoje")
