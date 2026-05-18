import cv2
import numpy as np
import matplotlib
matplotlib.use("Agg")  # backend nao-interativo (salva arquivo sem abrir janela)
import matplotlib.pyplot as plt

# Carregar imagem do repositorio em escala de cinza
img_original = cv2.imread("imagem_original.png", cv2.IMREAD_GRAYSCALE)
if img_original is None:
    raise FileNotFoundError("imagem_original.png nao encontrada na pasta do script")

# Aplicar equalizacao de histograma
img_equalizada = cv2.equalizeHist(img_original)

# Salvar imagem equalizada
cv2.imwrite("imagem_equalizada.png", img_equalizada)

# Plotar imagens e histogramas lado a lado
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Equalizacao de Histograma - OpenCV", fontsize=14)

axes[0, 0].imshow(img_original, cmap="gray", vmin=0, vmax=255)
axes[0, 0].set_title("Imagem Original (Baixo Contraste)")
axes[0, 0].axis("off")

axes[0, 1].imshow(img_equalizada, cmap="gray", vmin=0, vmax=255)
axes[0, 1].set_title("Imagem Equalizada (Contraste Expandido)")
axes[0, 1].axis("off")

axes[1, 0].hist(img_original.ravel(), bins=256, range=(0, 255), color="blue", alpha=0.7)
axes[1, 0].set_title("Histograma Original (concentrado)")
axes[1, 0].set_xlabel("Intensidade do Pixel")
axes[1, 0].set_ylabel("Frequencia")

axes[1, 1].hist(img_equalizada.ravel(), bins=256, range=(0, 255), color="green", alpha=0.7)
axes[1, 1].set_title("Histograma Equalizado (distribuido)")
axes[1, 1].set_xlabel("Intensidade do Pixel")
axes[1, 1].set_ylabel("Frequencia")

plt.tight_layout()
plt.savefig("resultado_equalizacao.png", dpi=100, bbox_inches="tight")
plt.close()

print("Equalizacao de histograma aplicada com sucesso!")
print("Arquivos salvos: imagem_equalizada.png, resultado_equalizacao.png")
