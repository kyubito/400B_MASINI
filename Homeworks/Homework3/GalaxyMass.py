import numpy as np
import astropy.units as u
from ReadFile import Read
import pandas as pd
from ReadFile import Read
def ComponentMass(X,Ptype) :

#    data = np.genfromtxt(X,dtype=None,names=True,skip_header=3)
    time,total,data = Read(X)


    index = np.where(data['type']==Ptype)

    mass = data['m'][index] *u.M_sun/100

    TotMass = np.around(sum(mass), decimals=3)

    return TotMass

#GalaxyName = np.array([MW, 'M31', 'M33'])
GalaxyName = ['MW', 'M31', 'M33']
HaloMass = [ComponentMass('MW_000.txt', 1), ComponentMass('M31_000.txt', 1), ComponentMass('M33_000.txt', 1)]
DiskMass =[ComponentMass('MW_000.txt', 2), ComponentMass('M31_000.txt', 2), ComponentMass('M33_000.txt', 2)]
BulgeMass = [ComponentMass('MW_000.txt', 3), ComponentMass('M31_000.txt', 3)]
Tot = [HaloMass[0]+DiskMass[0]+BulgeMass[0],HaloMass[1]+DiskMass[1]+BulgeMass[1], HaloMass[2]+DiskMass[2]]
LocalGroupMass = np.around(sum(HaloMass + DiskMass + BulgeMass), decimals=3)
StellarMatter = [(DiskMass[0]+BulgeMass[0]),DiskMass[1]+BulgeMass[1], (DiskMass[2]) ]
Frad = [((StellarMatter[0])/(Tot[0])), ((StellarMatter[1])/(Tot[1])), ((StellarMatter[2])/(Tot[2])), (sum(StellarMatter)/(LocalGroupMass))]


Table = np.array([GalaxyName, HaloMass, DiskMass, BulgeMass, Tot, LocalGroupMass, Frad])


print(Table)
