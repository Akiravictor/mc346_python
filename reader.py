def f():
	strike = 0
	reading = True
	print("Lendo")
	while reading:
		a = input()
		print(a)
		if (len(a) == 1):
			dfltMaxSpd = a[0]
			print("Velocidade Padrao: " + dfltMaxSpd)
		if (len(a) > 4):
			inicio = a[0]
			fim = a[2]
			nums = a[4:]
			print("inicio: " + inicio)
			print("fim: " + fim)
			print("dist e vel: " + nums)
		if (len(a) == 0):
			strike += 1
			if (strike > 1):
				reading = False