Implemetation of Dijkstra's algorithm to solve the following problem:

Given a set of cities (nodes), their roads linking each other (edges) and
the maximum speed at that road, return the fastest way from a city to another
```
INPUT Example:
25				//Maximum default speed
a b 1.3			//City A to City B have 1.3 km and its speed is the default speed
a c 1.6
a d 1.2
b e 1.5
c f 1.7
f c 1.7 35		//City F to City C have 1.7 km and its speed is 35km/h
d g 1.3
e f 1.6
e h 1.2
e i 1.5
f g 1.1
g j 1.7
h k 1.2
h i 1.5
i j 1.3
j i 1.3 30
i l 1.9
j k 1.6 50
j m 1.4 20
k n 2.2 30
l n 1.8
m n 1.2
				//blank line to split the 2nd part of input
a b 12			//Updating speed for road linking A to B to 12km/h
a c 10
e i 0			//Updating speed for road linking E to I to 0km/h, this means that this road is blocked
k n 5
a				//Starting point
n				//Ending point

OUTPUT Example:
17 minutos						//Time to travel from A to N
['a', 'd', 'g', 'j', 'm', 'n']	//Set of cities visited

Origem nao existe	//Starting point does not exist in the set of cities

Destino nao existe	//Ending point does not exist in the set of cities

Nao existe caminho de A para N fim	//There is no path from A to N
```