#import everything you need
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from functions import myfunction, myfunction2, myfunction3, chi_squared_fun, chi_squared_set, tag
style.use("ggplot")

#print statements
print("*")
print("*==============================*")
print("* BEGINNING SORTING ALGORITHM *")
print("*==============================*")
print '\n'

#open relevant JSON files and load them into defined variables
kf = open("tmp/pixels.json", "r")
ke = json.load(kf)
kf.close()

kg = open("tmp/klusters.json", "r")
kh = json.load(kg)
kg.close()

#open a text file to store relevant information
type_id = open("type_id.txt", "w")


#define empty lists you will need for the sorting algorithm below
ID = []
size = []
edgepixels = []
width = []
height = []
linearity = []
density = []
counts = []
m = []
residuals = []
radius = []
x_values = []
y_values = []
c_values = []
xy_values = []
c = []
#iterate over ke and kh to extract relevant information
#you can either append the information to an empty list or print them

for k in kh:
	ID.append(k['id'])
	size.append(k['size'])
	edgepixels.append(k['n_edgepixels'])
	width.append(k['width'])
	height.append(k['height'])
	linearity.append(k['lin_linearity'])
	density.append(k['density_uw'])
	counts.append(k['totalcounts'])
	m.append(k['lin_m'])
	residuals.append(k['lin_sumofres'])
	radius.append(k['radius_uw'])
	c.append(k['lin_c'])

for k in ke:
	x_values.append(k['x values'])
	y_values.append(k['y values'])
	c_values.append(k['c values'])
	xy_values.append(k['xy values'])

#sorting algorithm starts here

#initialize cluster types
slugs=0
loopers=0
branchers=0
crossovers=0
straight_wiggly=0
boxy=0
straight=0
curves=0

for i in range(len(edgepixels)):
	if size[i] > 19:
		if edgepixels[i] != size[i]:
			if density[i] > 0.1:
				if width[i]/height[i] > 1.3 or width[i]/height[i] < 0.7:
					slugs+=1
					type_id.write('\r\n')
					type_id.write("Type: Slug, ID: %s" % ID[i] )
					type_id.write('\r\n')
				else:
					boxy+=1
					type_id.write('\r\n')
					type_id.write("Type: Boxy  , ID: %s" % ID[i])
					type_id.write('\r\n')
		else:
			if myfunction(xy_values[i]) > 0:
				if size[i] > 50:
					if myfunction3(x_values[i],y_values[i]) > 0:
						crossovers+=1
						type_id.write('\r\n')
						type_id.write("Type: Crossover  , ID: %s" % ID[i])
						type_id.write('\r\n')
					else:
						if linearity[i] > 1:
							branchers+=1
							type_id.write('\r\n')
							type_id.write("Type: Brancher  , ID: %s" % ID[i])
							type_id.write('\r\n')

			else:
				if density[i] > 0.1:
					if counts[i]/size[i] < 25 and counts[i]/size[i] > 20:
						loopers += 1
						type_id.write('\r\n')
						type_id.write("Type: Looper , ID: %s" % ID[i])
						type_id.write('\r\n')
				
				else:
					if size[i]>100:
						if chi_squared_fun(x_values[i],y_values[i],m[i],c[i]) < 1:
							if tag(chi_squared_set(x_values[i],y_values[i],m[i],c[i])) == 1:
								straight_wiggly+=1
								type_id.write('\r\n')
								type_id.write("Type: Straight - Wiggly  , ID: %s" % ID[i])
								type_id.write('\r\n')
							else:
								straight+=1
								type_id.write('\r\n')
								type_id.write("Type: Straight  , ID: %s" % ID[i])
								type_id.write('\r\n')
						else:
							curves+=1
							type_id.write('\r\n')
							type_id.write("Type: Curves , ID: %s" % ID[i])
							type_id.write('\r\n')





#print the frequency of each cluster type
print("slugs: '%d '" % (slugs))
print("loopers: '%d '" % (loopers))
print("straight-wiggly: '%d '" % (straight_wiggly))
print("branchers: '%d '" % (branchers))
print("boxy: '%d '" % (boxy))
print("crossovers: '%d '" % (crossovers))
print("straight: '%d '" % (straight))
print("curves: '%d '" % (curves))

#create a bar graph for data visualisation

#initialize graph

objects = ('Slugs', 'Loopers', 'Branchers', 'SW', 'Boxy', 'Straight','Curves','Crossovers')
y_pos = np.arange(len(objects))
graphdata = [slugs,loopers,branchers,straight_wiggly,boxy,straight,curves,crossovers]
 
plt.bar(y_pos, graphdata, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.title('Frequency of Clusters')
 
plt.show()

type_id.close()

