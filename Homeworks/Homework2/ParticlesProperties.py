# First we import the modules we need
import numpy as np
import astropy.units as u
from ReadFile import Read

# Then we define the function
def ParticleInfo(X, Partype, number) :

#Call what data is :
    data = np.genfromtxt(X,dtype=None,names=True,skip_header=3) #Call back the data from the txt file

# define the number of particule needed
    n = number
# Introduce index to put the type into different category
    index = np.where(data['type']==Partype)

#Define the values we need for the position and velocity
    x = data['x'][index][n] * u.kpc
    y = data['y'][index][n] * u.kpc
    z = data['z'][index][n] * u.kpc
    vx = data['vx'][index][n] * (u.km)/(u.s)
    vy = data['vy'][index][n] * (u.km)/(u.s)
    vz = data['vz'][index][n] * (u.km)/(u.s)

# Define the values that need to be return by the function
    Mdistance = np.sqrt((x**2)+(y**2)+(z**2))
    Mvel = np.sqrt((vx**2)+(vy**2)+(vz**2))
    mass = data['m'][n]*u.M_sun

    return Mdistance, Mvel, mass #return the needed values

print(ParticleInfo('MW_000.txt', 2, 99)) # Print statement

# setting the values that correspond to the function itself
Mdistance, Mvel, mass = ParticleInfo('MW_000.txt', 2, 99)

#define a new distance to convert the unit from Kpc to Lyr
Mdistance2 = np.around(Mdistance.to(u.lightyear), decimals=3)

print(Mdistance2) #print statement

# The values we get for 1,2,3 and 4 are :
#(<Quantity 4.24484787 kpc>, <Quantity 312.1354934 km / s>, <Quantity 0.00394985 solMass>)
#13844.842053597764 lyr
#13844.842 lyr This is the rounded value to 3 decimal places.
