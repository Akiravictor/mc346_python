def f():
	strike = 0
	reading = True
	velMax = ""
	no_a = ""
	no_b = ""
	dist = ""
	vel = ""
	inicio = ""
	fim = ""
	atualiza_no_a = ""
	atualiza_no_b = ""
	nova_vel = ""
	print("Lendo")
	while reading:
		a = input()
		print("valor lido: " + a)
		print("len(a): " + str(len(a)))
		if (strike == 0):
			print("1a parte da entrada:")
			if (len(a) > 1 and ' ' not in a):
				velMax = a[0:]
			if (len(a) > 4):
				no_a = a[0]
				no_b = a[2]
				nums = a[4:]
				if (' ' in nums):
					esp = nums.index(' ')
					dist = nums[:esp]
					vel = nums[esp:]
				else:
					dist = nums
					vel = velMax
		else:
			print("2a parte da entrada:")
			if (len(a) == 1):
				if (inicio == ""):
					inicio = a[0]
				elif (inicio != "" and fim == ""):
					fim = a[0]
			if (len(a) > 1):
				atualiza_no_a = a[0]
				atualiza_no_b = a[2]
				nova_vel = a[4:]
		if (len(a) == 0):
			strike += 1
			if (strike > 1):
				reading = False
		print("Velocidade Padrao: " + velMax)
		print("No A: " + no_a)
		print("No B: " + no_b)
		print("Dist: " + dist)
		print("Vel: " + vel)
		print("Inicio: " + inicio)
		print("Fim: " + fim)
		print("Atualiza No A: " + atualiza_no_a)
		print("Atualiza No B: " + atualiza_no_b)
		print("Vel Nova: " + nova_vel)