
# coding: utf-8

# # In Class Lab 1
#
# ## Part A:  The Local Standard of Rest
# Proper motion of Sgr A* from Reid & Brunthaler 2004
# $\mu = 6.379$ mas/yr
#
# Peculiar motion of the sun, $v_\odot$ = 12.24 km/s  (Schonrich 2010)
#
#
# $v_{tan} = 4.74 \frac{\mu}{\rm mas/yr} \frac{R_o}{\rm kpc} = V_{LSR} + v_\odot$
#
#
# ### a)
#
# Create a function called VLSR to compute the local standard of res (V$_{LSR}$).
#
# The function should take as input: the solar radius (R$_o$), the proper motion (mu)
# and the peculiar motion of the sun in the $v_\odot$ direction.
#
# Compute V$_{LSR}$ using three different values R$_o$:
# 1. Water Maser Distance for the Sun :  R$_o$ = 8.34 kpc   (Reid 2014 ApJ 783)
# 2. GRAVITY Collaboration Distance for the Sun:  R$_o$ = 8.178 kpc   (Abuter+2019 A&A 625)
# 3. Value for Distance to Sun listed in Sparke & Gallagher : R$_o$ = 7.9 kpc
#

# In[ ]:


import numpy as np
# Fct to compute the local standard of rest velocity

# 4.75*mu*Ro = VLSR + vsun
# VLSR = 4.74*mu*Ro - vsun

def VLSR(Ro, mu=6.379, vsun=12.24) :
    # Inputs :
    #Ro=distance from the sun to galactic center (kpc)
    # mu is the proper motion of Sag A* (miliarcsec/yr) default is from Reid & Brunthaler 2004
    # vsun is the peculiar motion of the sun in the v direction (km/s) : default from Schonrich 2010
    # return :
    # VLSR le local standard of Rest (km/s)

    return 4.74*mu*Ro - vsun

RoReid = 8.34 # distance to galactic center from R et al 2014
RoGravity = 8.178 # distance to galactic center from GRAVITY Collaboration 2019
RoSG = 7.9 # distance to galactic center from textbook by Sparke and Gallagher

#compute VLSR using RoReid
VLSR_Reid = VLSR(RoReid)
print(VLSR_Reid)

#compute VLSR using RoGravity
VLSR_Gravity = VLSR(RoGravity)
print(VLSR_Gravity)

#compute VLSR using RoSG
VLSR_SG = VLSR(RoSG)
print(VLSR_SG)

#orbital period of the sun using Ro from GRAVITY Collaboration
# T = 2piR/V (kpc/km/s) --> Gyr
#v = vtan = VLSR + vsun

vtan = VLSR_Gravity + 12.24
T_Grav = 2*np.pi*RoGravity/vtan
print(T_Grav) # orbital period

# The number of rotations since begining of the universe
#
print(13.8/T_Grav)


# ### b)
#
# compute the orbital period of the sun using R$_o$ from the GRAVITY Collaboration (assume circular orbit)
#
# Note that 1 km/s $\sim$ 1kpc/Gyr

# ### c)
#
# Compute the number of rotations about the GC over the age of the universe (13.8 Gyr)

# ## Part B  Dark Matter Density Profiles
# The Grav constant is
G = 4.4988e-6
#compute the mass enclosed within the solar radius assuming an Isothermal Sphere model
#density profile rho = VLSR^2 / 4*pi*G*R^2
#Mass = Integrate Rho dV
#Integrate rho*pi*r^2dr
#Integrate VLSR^2 / (4*pi*G*r^2) * 4*pi*r^2 dr
#VLSR^2/G * r
def MassIso(r, VLSR=235) :
    #Inputs :
        # VLSR the local standard of rest (km/s) using default from VLSR from GRAVITY Collaboration
        #r is the distance from the galactic center
    #return :
        #Mass enclosed
    return VLSR**2/G*r




# ### a)
# Try out Fitting Rotation Curves
# [here](http://wittman.physics.ucdavis.edu/Animations/RotationCurve/GalacticRotation.html)
#
#
# ### b)
#
# In the Isothermal Sphere model, what is the mass enclosed within the solar radius (R$_o$) in units of $10^{10}$ M$_\odot$?
#
# Recall that for the Isothermal sphere :
# $\rho(r) = \frac{V_{LSR}^2}{4\pi G r^2}$
#
# Where $G$ = 4.4988e-6 kpc$^3$/Gyr$^2$/M$_\odot$
#
# What about at 260 kpc (in units of 10$^{12}$ M$_\odot$) ?


#compute mass enclosed within Ro
MIsoSolar = MassIso(RoGravity)
print(MIsoSolar/1e10) # units of 1e10 Msun

#compute mass enclosed within 260 kpc
MIso260 = MassIso(260)
print(MIso260/1e12)


# ## c)
#
# The Leo I satellite is one of the fastest moving satellite galaxies we know.
#
#
# It is moving with 3D velocity of magnitude: Vtot = 196 km/s at a distance of 260 kpc (Sohn 2013 ApJ 768)
#
# If we assume that Leo I is moving at the escape speed:
#
# $v_{esc}^2 = 2|\Phi| = 2 \int G \frac{\rho(r)}{r}dV $
#
# and assuming the Milky Way is well modeled by a Hernquist Sphere with a scale radius of $a$= 30 kpc, what is the minimum mass of the Milky Way (in units of $10^{12}$ M$_\odot$) ?
#
# How does this compare to estimates of the mass assuming the Isothermal Sphere model at 260 kpc (from your answer above)

#the potential for a Hernquist sphere
# Phi = - G*M/(r+a)
#Using the Hernquist Potential, the equation for Vesc becomes
#vesc^2 = 2*G*M/(r+a)

#Rearanging the esc eq for M
# M = vesc^2/2/G*(r+a)
#   = 196^2/2/G*(260+30)

#Fct that will determine the total halo mass needed to set a given esc at a given Distance
#assuming a Hernquist profile for the dark matter halo

def MassFromVesc(vesc,a,r) :
    #Inputs :
        #vesc the esc speed in km/s or speed satellite
        # r is the distance from the galactic center (kpc)
        # a = Hernquist scale length (kpc)
        # Return :
        # Total mass in Msun
        return vesc**2/2/G*(r+a)

MLeoI = MassFromVesc(196,30,260)
print(MLeoI/1e12)

print(MIso260/MLeoI)
