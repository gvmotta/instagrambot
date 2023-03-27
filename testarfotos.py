from PIL import Image
import shutil, os
img = Image.open(r'C:\Users\gusta\OneDrive\Área de Trabalho\bot\app\fotosenvios!\1.03-26-2023-15-37-352.jpg')

largura, altura = img.size

# calcular as coordenadas de início e fim para cortar a imagem no centro
esquerda = (largura - 1080) / 2
topo = (altura - 640) / 2
direita = (largura + 1080) / 2
inferior = (altura + 640) / 2

# cortar a imagem no centro
img_cortada = img.crop((esquerda, topo, direita, inferior))

# redimensionar as imagens para 1080 x 640 pixels
largura1 = 1080
altura1 = 640


img_cortada = img_cortada.resize((largura1, altura1))

# salvar a imagem cortada
img_cortada.save('imagem_cortada.jpg')

img_cortada.show()

op = int(input("1 para salvar na pasta envios\n2para excluir"))
if(op == 1):
    shutil.move(r'C:\Users\gusta\OneDrive\Imagens\app\imagem_cortada.jpg', r'C:\Users\gusta\OneDrive\Imagens\app\fotosenvios')
else:
    os.remove('imagem_cortada.jpg')