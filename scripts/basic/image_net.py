'''Baixando imagem'''
from requests import get

#colocando nome da imagem da internet
f = open('img.jpg','wb')

#Endereco da imagem na net
response = get('http://www.python.org/images/success/nasa.jpg')

#Abrindo imagem
f.write(response.content)

#Fechando imagem
f.close()
