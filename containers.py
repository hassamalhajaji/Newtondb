#every variable besides derivative
mechanicsVars = {
	#lowercase letters
	"v" : "velocity",
	"a" : "acceleration",
	"h" : "plancks constant",
	"m" : "mass",
	"g" : "gravity",
	"p" : "momentum",
	"v" : "velocity",
	"r" : "radius",
	"k" : "spring constant",
	"x" : "amount of extension",
	#uppercase letters
	"aa" : "area",
	"bb" : "elastic property",
	"ff" : "force",
	"ww" : "work",
	"jj": "joule",
	"pp" : "power",
	"ii" : "inertia",
	"ll" : "angular momentum",
	"hh" : "angular impulse",
	"gg" : "gravitational constant",
	"tt" : "period of pendulum",
	"ee" : "youngs modulus",
	"vv" : "volume",
	#greek letters (U for uppercase, L for lowercase)
	"alphaL" : "angular acceleration",
	"tauL" : "torque",
	"thetaU" : "angular position",
	"deltaU" : "difference",
	"etaU": "angular velocity",
	"omegaL" : ["angular frequency", "angular velocity"],
	"sigmaL" : "strain; uniaxial force per unit surface",
	"epsilonL": "stress; proportional deformation",
	"rho" : "inertial property",
	#subscripts
	"fs" : "static friction",
	"ll" : "angular momentum",
	"ii" : "moment of intertia",
	"fg" : "universal gravitation",
	"vg" : "gravitational potential",
	"fk" : "kinetic friction",
	"ac" : "centripetal acceleration",
	"uug" : "gravitational potential energy",
	"ein" : "energy in",
	"wwout" : "work out",
}





def f1(a, b):
	return a*b

def f2(a, b, c):
	return a*b*c

def f3(a, b, c, d):
	return a*b*c*d

def f4(e, f, g):
	return e+f+g

def f5(e, f, h):
	return e*f*h

equations = [f1, f2, f3, f4, f5]

input = ["alpha", "bravo"]









#output
"force"


mechanicsEqs = {}