import os
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'Pillow'])
    from PIL import Image

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'numpy==1.23.5'])
    import numpy as np

# Carrega a imagem
caminho_imagem = r'/content/imagem_satellite.jpeg'
imagem = Image.open(caminho_imagem)

dados = np.array(imagem)

quantidade_total_pixels = dados.size

quantidade_pixels_sem_dados = np.sum(dados == 0)

quantidade_pixels_soja = np.sum(dados == 39)

quantidade_pixels_pastagem = np.sum(dados == 15)

quantidade_pixels_validos = quantidade_total_pixels - quantidade_pixels_sem_dados

# Área total do Brasil em hectares (segundo o IBGE)
area_brasil_hectares = 851576700  # em hectares

percentual_soja = quantidade_pixels_soja / quantidade_pixels_validos
percentual_pastagem = quantidade_pixels_pastagem / quantidade_pixels_validos

area_soja_hectares = percentual_soja * area_brasil_hectares
area_pastagem_hectares = percentual_pastagem * area_brasil_hectares

print(f"Quantidade total de pixels da imagem: {quantidade_total_pixels}")
print(f"Quantidade de pixels sem dados (código 0): {quantidade_pixels_sem_dados}")
print(f"Quantidade de pixels correspondente ao plantio de soja (código 39): {quantidade_pixels_soja}")
print(f"Quantidade de pixels correspondente a pastagem (código 15): {quantidade_pixels_pastagem}")
print(f"\nÁrea de plantio de soja: {area_soja_hectares:.2f} hectares (contagem de pixels: {quantidade_pixels_soja})")
print(f"Área de cobertura de pastagem: {area_pastagem_hectares:.2f} hectares (contagem de pixels: {quantidade_pixels_pastagem})")