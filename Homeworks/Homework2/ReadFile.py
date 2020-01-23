import numpy as np
import astropy.units as u

def Read(MW_000) :
	file = open(MW_000,'r' )
	line1 = file.readline()
	label, value = line1.split()
	time = float(value)*10.0*u.Myr
	line2 = file.readline()
	label, value = line2.split()
	total = float(value2)*10.0*u.m
	data = np.genfromtxt(MW_000,dtype=None,names=True,skip_header=3)
	return(time, total, data)
	print(time, total, data)
	file.close()
