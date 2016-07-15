#define a function to be placed in process-frames.py
#function will take on values klusterid, kl and outputpath. we note that these are dummy variables.
#function is called on in line 216 in process-frames.py
def getsomething(klusterid, kl, outputpath):
	#define a dictionary to extract all the pixel information. note that pixelMap is a dictionary
	pixel_map = kl.getPixelMap()
	#define a list to get the number of pixels aka size
	g = kl.getNumberOfPixels()
	#define 3 lists to take in x,y and C values of the pixels
	x_values = []
	y_values = []
	C_values = []
	xy_values = []
	#iterate over pixel_map dict to extract the x,y and c information. note that X = x + 256y
	for X, C in pixel_map.iteritems():
		x = X%256
		y = X/256
		x_values.append(x)
		y_values.append(y)
		C_values.append(C)

	xy_values = zip(x_values,y_values)	
	#create a list of information to be printed or written into a text/JSON file. 
	#refer to kluster.py lines 370 to 398 if more information is required and type accordingly
	#this is the information we want so we return p
	p = {
    "ID"			: klusterid, 					\
    #"pixels"        : kl.getPixelMap(),             \
    #"size"          : kl.getNumberOfPixels(),       \
    "x values" 		: x_values,						\
    "y values" 		: y_values,						\
    "c values"		: C_values,						\
    "xy values"		: xy_values						\
	}
	return p