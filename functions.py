import collections

def chi_squared_fun( x_value_O, y_value_O, M , C):
	
	x_value_o = []
	y_value_o = []
	
	if abs(M) > 1 :
		x_value_o = y_value_O
		y_value_o = x_value_O
		m = 1/M
		c = -(C/M)
		
	
	else:
		x_value_o = x_value_O
		y_value_o = y_value_O
		m = M
		c = C


	y_value_e = []
	chi_sq = 0
	lin_m = m
	lin_c = c

	
	for j in range(len(x_value_o)):
		b = lin_m*x_value_o[j] + lin_c
		y_value_e.append(b)

		if abs(y_value_e[j]) > 0.000001:
			
			delta = y_value_o[j] - y_value_e[j]
			deltasqu = delta ** 2
			chi_j = deltasqu / y_value_e[j]
			chi_sq = chi_sq + chi_j

		else:
			y_value_e[j] = 0.000001
			delta = y_value_o[j] - y_value_e[j]
			deltasqu = delta ** 2
			chi_j = deltasqu / y_value_e[j]
			chi_sq = chi_sq + chi_j
		
	chi_squ_red = chi_sq / 2
	
	return chi_squ_red
	
def chi_squared_set( x_value_O, y_value_O, M , C):
	
	x_value_o = []
	y_value_o = []
	
	if abs(M) > 1 :
		x_value_o = y_value_O
		y_value_o = x_value_O
		m = 1/M
		c = -(C/M)
		
	
	else:
		x_value_o = x_value_O
		y_value_o = y_value_O
		m = M
		c = C
		
	chi_squ_set = []
	chi_squ_red = 0
	
	t = len(x_value_o)
	
	r = t/50
	
	for i in range(r+1):
		
		x_value_o1 = []
		y_value_o1 = []
		x_value_o2 = []
		y_value_o2 = []
		
		j = (i+1)*50


		if j <= t :
			
			for n in range(j):
				x_value_o1.append(x_value_o[n])
				y_value_o1.append(y_value_o[n])
			
				
		elif j > t :
			
			j = t

			for n in range(j):
				x_value_o1.append(x_value_o[n])
				y_value_o1.append(y_value_o[n])
			
			
		my_tuple = zip(x_value_o1,y_value_o1)
		my_tuple2 = sorted(my_tuple, key=lambda x: x[0])

		
		for l in range(j):
			x_value_o2.append(my_tuple2[l][0])
			y_value_o2.append(my_tuple2[l][1])
		


		y_value_e2 = []
		chi_sq = 0
		lin_m = m
		lin_c = c

		
		for s in range(len(x_value_o2)):
			b = lin_m*x_value_o2[s] + lin_c
			y_value_e2.append(b)

			if abs(y_value_e2[s]) > 0.000001:
				
				delta = y_value_o2[s] - y_value_e2[s]
				deltasqu = delta ** 2
				chi_j = deltasqu / y_value_e2[s]
				chi_sq = chi_sq + chi_j

			else:
				y_value_e2[s] = 0.000001
				delta = y_value_o2[s] - y_value_e2[s]
				deltasqu = delta ** 2
				chi_j = deltasqu / y_value_e2[s]
				chi_sq = chi_sq + chi_j
				
		chi_squ_red = chi_sq / 2	
		chi_squ_set.append(chi_squ_red)

	return chi_squ_set
	
def tag(chi_squared_set):
	
	tag = 0

	for i in range(1,len(chi_squared_set)):
		delta_chi = chi_squared_set[i] - chi_squared_set[i-1]
	
		if delta_chi > 0.3 :
			tag = 1
			break
			
	return tag

def myfunction(xytuple):
	#get all x values out
	b = [x[0] for x in xytuple]
	#get repeated x values
	c = [item for item, count in collections.Counter(b).items() if count > 1]
	d = []
	f = []
	#search for corresponding y value
	for i in range(len(c)):
		for xy in xytuple:
			if xy[0] == c[i]:
				d.append(xy)
				#d is a list of tuples with repeated x values

	for i in range(len(d)):
		g = []
		for x in d:
			if x[0] == d[i][0]:
				g.append(x)
				if len(g) > 1:
					i =0
					while i+1<(len(g)):
						if g[i][1] - g[i+1][1] > 3:
							f.append(g[i])
							f.append(g[i+1])
						i += 1



	return len(f)

def myfunction2(xytuple):
	#get all y values out
	b = [x[1] for x in xytuple]
	#get repeated y values
	c = [item for item, count in collections.Counter(b).items() if count > 1]
	d = []
	f = []
	#search for corresponding y value
	for i in range(len(c)):
		for xy in xytuple:
			if xy[1] == c[i]:
				d.append(xy)
				#d is a list of tuples with repeated y values

	for i in range(len(d)):
		g = []
		for x in d:
			if x[1] == d[i][1]:
				g.append(x)
				if len(g) > 1:
					i =0
					while i+1<(len(g)):
						if g[i][0] - g[i+1][0] > 3:
							f.append(g[i])
							f.append(g[i+1])
						i += 1


	return len(f)



def myfunction3(x,y):
	xy =  zip(x,y)
	xy2 = sorted(xy, key=lambda x: x[0])
 	
	seen = set()
	keep = []
	for filename, filepath in xy2:
		if filename in seen:
			continue
		else:
			seen.add(filename)
			keep.append((filename, filepath))

	b = [x[1] for x in keep]
	c = [item for item, count in collections.Counter(b).items() if count > 1]
	d = []
	f = []

	for i in range(len(c)):
		for xy in keep:
			if xy[1] == c[i]:
				d.append(xy)


	for i in range(len(d)):
		g = []
		for x in d:
			if x[1] == d[i][1]:
				g.append(x)
				if len(g) > 1:
					i =0
					while i+1<(len(g)):
						if abs(g[i][0] - g[i+1][0]) > 20:
							f.append(g[i])
							f.append(g[i+1])
						i += 1
	return len(f)

