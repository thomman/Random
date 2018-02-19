#Finds the k closest points to the origin given an array of tuples.

def close(a, k):
	d = {}
	from math import sqrt
	for point in a:
		x = point[0]
		y = point[1]
		d[point] = round(sqrt(x*x + y*y), 3)
	return [l for l in sorted(d, key=d.__getitem__)[:k]]

#Expect the three closest points
#a = [(-2,4),(0,2),(5,3),(7,9),(80,3)]
#print(close(a,3))
