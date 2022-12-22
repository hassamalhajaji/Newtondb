################ List of Variables ################

import math

mechanicsVars = {
	#lowercase letters
   	"initial position" : "di",
   	"final position" : "df"
    	"dipslacement" : "d",
    	"height" : "hi"
    	"time" : "t",
	"length" : "l",
    	"velocity" : "v",
    	"initial velocity" : "vi",
    	"final velocity" : "vf",
    	"average velocity" : "va",
    	"acceleration" : "a",
	"plancks constant" : "h",
	"angle" : "theta" # degrees 
	"mass" : "m",
	"gravity" : "g", # at surface
	"momentum" : "p",
	"initial momentum" : "pi",
	"final momentum" : "pf",
	"radius" : "r",
    	"impulse" : "imp",
	"force" : "ff",
	"work" : "ww" ,
    	"rotational work" : "wwr"
    	"rotational power" : "pwr"
    	"rotational kinetic energy" : "ker"
	"power" : "pp" ,
	"inertia" : "ii" ,
	"angular momentum" : "ll",
	"angular impulse" : "hh",
    	"angular velocity" : "w"
	"force of gravity" : "g",
	"Period": "tt",
    	"weight" : "wei",
    	"energy" : "en",
	"final energy" : "enf",
	"initial energy" : "eni",
    	"coefficient of static friction" : "us",
    	"coefficient of kinetic friction" : "uk",
    	"static force" : "fs",
    	"kinetic force" : "fk",
    	"normal force" : "fn"
	"spring force" : 'fsp"
    	"centripetal acceleration" : "ac",
    	"angular acceleration" : "alpha",
    	"torque" : "tau",
    	"kinetic energy" : "ke",
    	"initial potential energy":"pei",
    	"final potential energy":"pef",
    	"potential" : "pe",
	"spring potential" : "ps"
	"gravatational force" : "fg"
	"first mass" : "m1", # multibody
	"second mass" : "m1",
	"spring constant" : "ks"
	"frequency" : "f",
	"density" : "den",
	"volume" : "vol",
	"pressure" : "pr",
	"area" : "area",
	"wavelength" : "lam",
	"index of refraction" : "n",
	"incident n" : "ni",
	"transmitted n" : "nt",
	"incident theta" : "thetai",
	"transmitted theta" : "thetat",
	"focal length" : "fok",
	"distance to object" : "obd",
	"distance to image" : "imd",
	"radius of curvature" : "rcur",
}



################ List of constants ################ 
################ http://physics.nist.gov/cuu ################ 

# Speed of light in vacuum
c = 299792458 ,  # m/s 

# Gravitational constant
Gc = 6.67430e-11, # N (m**2 / kg**2)

# Planks constant
h = 6.62607015e-34  # Js

# Dirac constant H bar
hb = 1.054571817e-34 # Js

# elementray charge 
e = 1.602176634e-19 # C

# permitivitty of free space 
e0 = 8.8541878128e-12 # C**2/N m**2

# Fine structure constant 
fsc = e**2 / (4*pi*e0*hb*c) # approx 1/137

# Bohr magneton
ub = e*hb / 2*mp

# Rydberg constant 
rb = fsc**2 *me*c / 2h # 1/m

# Boltzmann constant
k = 1.380649-23 # J/K

# Avogadro constant
na = 6.02214076e23 # 1/mol

# Gas Constant
Rc = na*k # 8.314462618 J/mol K

# Stefan-Boltzmann constant 
sb = 5.670374419e-8 # W/m**2 K**4

# atomic mass constant
mu =  1.66053906660e-27 # kg

# electron mass
me =  9.1093837015e-31 # kg

# proton mass
mp =  1.66053906660e-27 # kg

# neutron mass
mn =  1.67492749804e-27 # kg

# luminous efficacy
kcd = 683 # lm/W



################ List of equations ################

def velocity(d, t, v):
    #Check which variable is missing
    v = d/t
    #Rewrite equation as a fucntion of the missing variable
    #Return missing variable
    return v

def velocity2(vf, vi, a, t):
    v = vi + a*t
    return v

def velocity3(vf, vi, a, t, di):
    vf = di + vi*t + (1/2)*a*t
    return vf

def velocity4(vi, a, di, df):
    vf = sqrt(vi**2 + 2*a*(df-di))
    return vf

def velocityavg(vf, vi, va):
    va = (1/2)*(vf + vi)
    return va

def displacement(di,df,d):
    d = df - di
    return d

def velocity(vf, vi, v):
    v = vf - vi
    return v

def acceleration(v, t, a):
    a = v/t
    return a

def weight(m, g, wei):
    wei = m*g
    return wei

def frictionstatic(us,fn, fs):
    fs <= us*fn
    return fs

def frictionkinetic(uk,fn, fs):
    fk <= uk*fn
    return fk

def cenaccel(v,r,ac):
    ac = (v**2)/r
    return ac

def cenaccel2(w,r,ac):
    ac = (w**2)*r
    return ac

def momentum(m, a, ff):
    ff = m*a
    return ff

def weight(m, g, wei):
    wei = m*g
    return wei

def cenaccel(v, r, ac):
    ac = (v**2)/r
    return ac

def momentum(m, v, p):
    p = m*v
    return p

def impulse(ff, t):
    imp = ff*t
    return imp

def work(ff, d, ww):
    ww = ff*d
    return ww

def workenergy(m, g):
    en = ff*d
    return en

def kineticenergy(m,v,ke):
    ke = (1/2)*m*v**2
    return ke

def forcepotential(pei,pef,ff):
    ff = pef - pei
    return ff

def potential(pei,pef,pe):
    pe = pef - pei
    return pe

def energy(enf,eni,en):
    en = enf - eni
    return en

def gravpotentialenergy(m,g,hi):
    pe = m*g*hi
    return pe

def power(ww, t,pw):
    pw = ww/t
    return pw

def powervelocity(pw, v, ff):
    pw = ff*v
    return pw

def angularvelocity(theta, t, w):
    w = theta/t
    return pw

def angularacc(alpha,w,t):
    alpha = w/t
    return alpha

def torque(r,ff):
    tau = r*ff
    return tau

def momentofI(ine,m,r):	
    ine = m*r**2
    return ine

def workrotation(tau,theta,wwr):
    wwr = tau*theta,
    return wwr

def powerrotation(tua,w,pwr):
    pwr = tau*w
    return pwr

def gravitationalforce(fg,gc,m1,m2,r):
    fg = gc*(m1*m2/r**2)
    return fg

def gravitationalforce(fg,gc,m1,m2,r):
    fg = gc*(m1*m2/r**2)
    return fg

def gravitationalfield(gf,gc,m1,m2,r):
    fg = gc*(m1*m2/r**2)
    return fg
		
def springforce(fsp,ks,d):
    fsp = -ks*d
    return fsp

def springpotentiale(ps,d,ks):
    ps = (1/2)*ks*d**2
    return ps

def sho(tt,m,ks):
    tt = 2*pi*sqrt(m/ks)
    return tt

def simplependulum(tt,g,l):
    tt = 2*math.pi*sqrt(l/g)
    return tt

def frequency(tt):
    f = 1/tt
    return f

def frequencyangular(f):
    w = 2*math.pi*f
    return w

def density(m,vol):
    den = m/vol
    return den

def pressure(ff,area):
    pr = ff/area
    return pr

def velocityfrequency(f,v,lam):
    v = f/lam
    return v

def interferencewave(n,d,lam,theta):
    lam = d*sin(theta)/n
    return lam

def indexofn(n,v):
    n = c/v
    return n

def goodoldsnelli(ni,nt,thetai,thetat):
    ni = nf*sin(thetat) / sin(thetai)
    return ni

def criticalangle(thetac,ni,nt):
    thetac = math.asin(nt/ni) # issue with rewrite
    return thetac

def criticalangle(thetac,ni,nt):
    thetac = math.asin(nt/ni)
    return thetac

def images(obd,imd,fok):
    fok = obd*imd / (imd + obd)
    return fok	

def focalsphere(fok,rcur):
    fok = rcur/2
    return fok
