


#every variable besides derivative
mechanicsVars = {
	#lowercase letters
   	"initial position" : "di",
   	"final position" : "df"
    	"dipslacement" : "d",
    	"height" : "hi"
    	"time" : "t",
    	"velocity" : "v",
    	"initial velocity" : "vi",
    	"final velocity" : "vf",
    	"average velocity" : "va",
    	"acceleration" : "a",
	"plancks constant" : "h",
	"angle" : "theta"
	"mass" : "m",
	"gravity" : "g",
	"momentum" : "p",
	"initial velocity" : "pi",
	"final velocity" : "pf",
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
    	"centripetal acceleration" : "ac",
    	"angular acceleration" : "alpha",
    	"torque" : "tau",
    	"kinetic energy" : "ke",
    	"initial potential energy":"pei",
    	"final potential energy":"pef",
    	"potential" : "pe",

}


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
    vf**2 = vi**2 + 2*a*(df-di)
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
