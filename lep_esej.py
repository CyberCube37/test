with open('esej.txt') as esej:
	manj_kot3 = 0
	vec_kot8 = 0
	dolzina = 0
	prev = ''
	for vrstica in esej:
		vrstica += ' '
		for znak in vrstica:
			if znak.isalpha():
				dolzina += 1
			elif prev.isalpha():
				if dolzina < 3:
					manj_kot3 += 1
				if dolzina > 8:
					vec_kot8 += 1
				dolzina = 0
			prev = znak
if manj_kot3 == 0 and vec_kot8 ==0:
	print('lep esej')
else:
	print('manj kot 3:', manj_kot3)
	print('vec kot 8:', vec_kot8)
	