import numpy as np

thickness = 1

# nodes = np.array([
# 	[33, 16, -2],
# 	[66, 16, -1.5],
# 	[99, 16, -1],
# 	[132, 16, -0.5],
# 	[165, 16, 0.0],
# 	[198, 16, 0.5],
# 	[231, 16, 1],
# 	[264, 16, 1.5],
# 	[297, 16, 2]
# ])
#
# traction = np.array([
# 	[33, 0, 0],
# 	[66, 0, -164.0625],
# 	[99, 0, -281.2500],
# 	[132, 0, -351.5625],
# 	[165, 0, -375.0000],
# 	[198, 0, -351.5625],
# 	[231, 0, -281.2500],
# 	[264, 0, -164.0625],
# 	[297, 0, 0]]) # A sequence of node must be in this list

nodes = np.array([
	[103,       20.0,       0.0],
	[928,		20.0,		0.200000003],
	[929,		20.0,		0.400000006],
	[930,		20.0,		0.600000024],
	[931,		20.0,		0.800000012],
	[932,		20.0,		1.0],
	[933,		20.0,		1.20000005],
	[934,		20.0,		1.39999998],
	[935,		20.0,		1.60000002],
	[936,		20.0,		1.79999995],
	[937,		20.0,		2.0],
	[938,		20.0,		2.20000005],
	[939,		20.0,		2.4000001],
	[940,		20.0,		2.5999999],
	[941,		20.0,		2.79999995],
	[942,		20.0,		3.0],
	[943,		20.0,		3.20000005],
	[944,		20.0,		3.4000001],
	[945,		20.0,		3.5999999],
	[946,		20.0,		3.79999995],
	[947,		20.0,		4.0],
	[948,		20.0,		4.19999981],
	[949,		20.0,		4.4000001],
	[950,		20.0,		4.5999999],
	[951,		20.0,		4.80000019],
	[104,		20.0,		5.0]])


traction = np.array([
	[103, 0, -0.25],
	[928, 0, -0.25],
	[929, 0, -0.25],
	[930, 0, -0.25],
	[931, 0, -0.25],
	[932, 0, -0.25],
	[933, 0, -0.25],
	[934, 0, -0.25],
	[935, 0, -0.25],
	[936, 0, -0.25],
	[937, 0, -0.25],
	[938, 0, -0.25],
	[939, 0, -0.25],
	[940, 0, -0.25],
	[941, 0, -0.25],
	[942, 0, -0.25],
	[943, 0, -0.25],
	[944, 0, -0.25],
	[945, 0, -0.25],
	[946, 0, -0.25],
	[947, 0, -0.25],
	[948, 0, -0.25],
	[949, 0, -0.25],
	[950, 0, -0.25],
	[951, 0, -0.25],
	[104, 0, -0.25]]) # A sequence of node must be in this list

rows, columns = np.shape(traction)

loading = np.zeros([rows, columns-1])

for i in range(rows-1):
	node1 = nodes[i, 1:]
	node2 = nodes[i+1, 1:]
	L = np.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)
	T1 = L/2.0 * thickness * traction[i, 1:]
	T2 = L/2.0 * thickness * traction[i+1, 1:]
	loading[i, :] += T1
	loading[i+1, :] += T2

# Check input
outputpath = './traction.dat'
# Open output file to write
outputfile = open(outputpath, 'a+')
outputfile.write('<NodeConstraints>\r')
for i in range(rows):
	strg1 = 'u[' + str(int(traction[i, 0])-1) + '] = ' + str(loading[i, 0]) + ';\r'
	outputfile.write(strg1)
	strg2 = 'v[' + str(int(traction[i, 0])-1) + '] = ' + str(loading[i, 1]) + ';\r'
	outputfile.write(strg2)
outputfile.write('</NodeConstraints>\r')