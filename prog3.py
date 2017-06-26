def fMain():
	strike = 0
	reading = True
	dic = {}
	nos = []
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
	#print("Lendo")
	while reading:
		a = input()
		#print("valor lido: " + a)
		#print("len(a): " + str(len(a)))
		if (strike == 0):
			#print("1a parte da entrada:")
			if (len(a) > 1 and ' ' not in a):
				velMax = a[0:]
			if (len(a) > 4):
				no_a = a[0]
				no_b = a[2]
				nums = a[4:]
				if (' ' in nums):
					esp = nums.index(' ')
					dist = nums[:esp]
					esp += 1
					vel = nums[esp:]
				else:
					dist = nums
					vel = velMax
				buildDict(dic,no_a,no_b,dist,vel)
				if (no_a not in nos):
					nos.append(no_a)
				if (no_b not in nos):
					nos.append(no_b)
		else:
			#print("2a parte da entrada:")
			if (len(a) == 1):
				if (inicio == ""):
					inicio = a[0]
					if (inicio not in nos):
						print("Origem nao existe")
				elif (inicio != "" and fim == ""):
					fim = a[0]
					if (fim not in nos):
						print("Destino nao existe")
					reading = False
			if (len(a) > 1):
				atualiza_no_a = a[0]
				atualiza_no_b = a[2]
				nova_vel = a[4:]
				buildDict(dic, atualiza_no_a, atualiza_no_b, "0", nova_vel)
				nova_vel = ""
		if (len(a) == 0):
			strike += 1
			if (strike > 1):
				reading = False
		#print("Velocidade Padrao: " + velMax)
		#print("No A: " + no_a)
		#print("No B: " + no_b)
		#print("Dist: " + dist)
		#print("Vel: " + vel)
		#print("Inicio: " + inicio)
		#print("Fim: " + fim)
		#print("Atualiza No A: " + atualiza_no_a)
		#print("Atualiza No B: " + atualiza_no_b)
		#print("Vel Nova: " + nova_vel)
		#print("Dic: " + str(dic))
		#print("Nos: " + str(nos))
	#graph = {k:v for k, v in buildGraph(dic,nos).items() if v}
	graph = buildGraph(dic,nos)
	#print(str(graph))
	prev = shortPath(graph,nos,inicio,fim)
	
	if (prev != None):
		caminho = []
		buildPath(prev, fim, caminho)
		print(str(caminho))

		
def buildDict(dic, no_a, no_b, dist, vel):
	if(dist != "0"):
		dic["(" + no_a + "," + no_b + ")"] = (dist,vel)
	if(vel != "0"):
		(dist_antiga, vel_antiga) = dic["(" + no_a + "," + no_b + ")"]
		#print("dist_antiga: " + dist_antiga + "\nvel_antiga: " + vel_antiga)
		dic["(" + no_a + "," + no_b + ")"] = (dist_antiga, vel)
	if(vel == "0"):
		del dic["(" + no_a + "," + no_b + ")"]
	
def buildGraph(dic, nos):
	import re
	g = {}
	for i in nos:
		d = {}
		for j in dic:
			if (re.match("\("+str(i)+",[a-z]\)",str(j))):
				(dist,vel) = dic[j]
				tempo = float(dist)/float(vel)
				tempo = tempo * 60
				d[j[3]] = tempo
		g[i] = d
	#print(str(g))
	return g
	
def buildPath(prev, fim, path):
	if (prev[fim] != '-'):
		buildPath(prev, prev[fim], path)
		path.append(fim)
	else:
		path.append(fim)
	
def shortPath(graph, nos, inicio, fim):
	import sys
	import math as m
	dist = {}
	prev = {}
	for i in nos:
		dist[i] = sys.maxsize
		prev[i] = "-"
	dist[inicio] = 0

	while nos:
		min = m.inf
		no = ""
		for i in dist:
			if (min >= dist[i] and str(i) in nos):
				min = dist[i]
				no = i

		nos.remove(no)

		vizinhos = []
		dic_viz = graph[no]
		for i in graph[no]:
			vizinhos.append(i)

			for i in vizinhos:
				alt = dist[no] + dic_viz[i]
				if (alt < dist[i]):
					dist[i] = alt
					prev[i] = no

	#print(str(graph))
	#print(str(dist))
	if (dist[fim] == sys.maxsize):
		print("Nao existe caminho de " + inicio + " para " + fim)
		return None
	else:
		print(str(int(dist[fim])) + " minutos")
		return prev

if __name__ == "__main__":
	fMain()