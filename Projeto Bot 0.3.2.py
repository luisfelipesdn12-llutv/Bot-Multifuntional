#COPIA do @quadnite_bot, feita por Luis Felipe para APRENDIZAGEM da linguagem Python
#COPY of @quadnite_bot, made by Luis Felipe for LEARNING of the Python language.
from random_words import RandomWords
rw = RandomWords()
import morse_talk as mtalk
from random import choice
from random import randint
from time import sleep
comandoslist = ['comandos', 'palavra', 'palavras', 'moeda', 'paramorse', 'morsepara', 'parabin', 'binpara', 'absurdificar']
#funçoes:
def comandos():
	print("COMANDOS DISPONÍVEIS:\n")
	for comando in comandoslist:
		if comando != comandoslist[0]:
			print(f'/{comando}')
	print()
def palavra():
	print(rw.random_word())
def palavras(n):
	try: palavraslist = rw.random_words(letter=n)
	except: palavraslist = rw.random_words(count=n)
	for palavra in palavraslist:
		print(palavra)
def moeda():
	possibilidadeslist = ["CARA", "COROA"]
	print(choice(possibilidadeslist))
def paramorse(text):
	print(mtalk.encode(text))
def morsepara(text):
	print(mtalk.decode(text))
def parabin(text):
	print(mtalk.encode(text, encoding_type='binary'))
def binpara(text):
	print(mtalk.decode(text, encoding_type='binary'))
def absurdificar(text):
	for letra in text:
		tamanho = randint(1, 2)
		if tamanho == 1: print(letra.upper(), end='')
		if tamanho == 2: print(letra.lower(), end='')
	print()
comandosdict = {"comandos": comandos, "palavra" : palavra,
"palavras": palavras, "moeda": moeda, "paramorse": paramorse, "morsepara":morsepara,
"parabin": parabin, "binpara":binpara, "absurdificar":absurdificar}
#looping infinito para inserção de comandos (ainda vou colocar um break)
while True:
	user = input("\033[33m-> /")
	print("\033[m", end = "")
	try: comando = user[:user.index(" ")]
	except: comando = user
	try: parametro = user[(user.index(" ") + 1):]
	except: parametro = None
	try:
		comandofunc = comandosdict[comando]
		if parametro != None:
			try: comandofunc(parametro)
			except: comandofunc(int(parametro))
		else: comandofunc()
	except: print("Comando ou Parâmetro Inválido. Digite o /comandos para receber a lista de comandos disponíveis.")