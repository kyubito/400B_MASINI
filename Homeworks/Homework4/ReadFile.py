import numpy as np
import astropy.units as u

def Read(X) :
	file = open(X,'r' )
	line1 = file.readline()
	label, value = line1.split()
	time = float(value)*10.0*u.Myr

	line2 = file.readline()
	label2, value2 = line2.split()
	total = float(value2)

	file.close()
	data = np.genfromtxt(X,dtype=None,names=True,skip_header=3)
	return time, total, data

time, total, data = Read('MW_000.txt')

#print((data['x'][1]))
