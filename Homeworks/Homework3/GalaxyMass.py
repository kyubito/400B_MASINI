import numpy as np
import astropy.units as u
from ReadFile import Read
import pandas as pd
from ReadFile import Read
def ComponentMass(X,Ptype) :

#    data = np.genfromtxt(X,dtype=None,names=True,skip_header=3)
    time,total,data = Read(X)


    index = np.where(data['type']==Ptype)

    mass = data['m'][index] *u.M_sun

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

# table = pd.DataFrame()
#
# table['Galaxy Name'] = GalaxyName
# table['Halo Mass ($10^{12} M_{\odot}$)'] = HaloMass
# table['Disk Mass ($10^{12} M_{\odot}$)'] = DiskMass
# table['Bulge Mass ($10^{12} M_{\odot}$)'] = BulgeMass
# table['Total Mass ($10^{12} M_{\odot}$)'] = Tot
# table['Local Group Mass ($10^{12} M_{\odot}$)'] = LocalGroupMass
# table['Baryon Fraction ($10^{12} M_{\odot}$)'] = Frad


print(Table)








# print(ComponentMass('MW_000.txt', 1), 'Mass Halo Milky Way')
# print(ComponentMass('MW_000.txt', 2), 'Mass Disk Milky Way')
# print(ComponentMass('MW_000.txt', 3), 'Mass Bulge Milky Way')
# print(ComponentMass('M31_000.txt', 1), 'Mass Halo M31')
# print(ComponentMass('M31_000.txt', 2), 'Mass Disk M31')
# print(ComponentMass('M31_000.txt', 3), 'Mass Bulge M31')
# print(ComponentMass('M33_000.txt', 1), 'Mass Halo M33')
# print(ComponentMass('M33_000.txt', 2), 'Mass Disk M33')
