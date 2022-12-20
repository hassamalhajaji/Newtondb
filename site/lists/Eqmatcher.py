#PREFILLED DUMMY VARIABLES, EQUATIONS, AND INPUT ########################################################
import inspect 

# variables = {"alpha":"a", "bravo":"b", "charlie":"c", "delta":"d", 
# "echo":"e", "foxtrot":"f", "golf":"g", "hotel":"h"}

variables = {"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta", 
"e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel"}

def f0(a):
	return a

def f1(a, b):
	return a+b

def f2(a, b, c):
	return a+b+c

def f3(a, b, c, d):
	return a+b+c+d

def f4(a, b, c, d, e):
	return a+b+c+d+e

def f5(e, f, g):
	return e*f*g

equations = [f0, f1, f2, f3, f4, f5]

inputs = ["alpha", "bravo", "charlie"]
inputs = set(inputs) #make sure there's no duplicates! for computation safety!
#also need code to check if the inputs are actual variables in variable dictionary

#FUNCTION THAT IS THE FOCUS ####################################################

'''
~~~	EQUATION MATCHER V.1 ~~~
What is the role of the n? N is a range configurator 
N is zero:
	if n = 0, it returns a list of equations (functions) that take in exactly the same amount of variables from input
	eg. input = ["alpha", "bravo", "charlie"] --> returns [f2]
N is positive:
		You want a list of equations that require the same amount of variables you have
		or that require the variables you have + more (adjustable with n); "Functions I am short with variables on"
			if n = 1, it returns a list of equations (functions) that require at most 1 more variable to be solved
			eg. input = ["alpha", "bravo", "charlie"] --> returns [f2, f3]
			if n = 2, it returns a list of equations (functions) that require at most 2 more variables to be solved
			eg. input = ["alpha", "bravo", "charlie"] --> returns [f2, f3, f4]
N is negative:
		You want a list of equations that require the same amount of variables you have
		or that require less than the variables you have (adjustable with n); "Functions I exceed with variables on"
			if n = -1, it returns a list of equations (functions) that require at most 1 less variable to be solved
			eg. input = ["alpha", "bravo", "charlie"] --> returns [f1, f2]
			if n = -2, it returns a list of equations (functions) that require at most 2 less variables to be solved
			eg. input = ["alpha", "bravo", "charlie"] --> returns [f0, f1, f2]

The role of the equationMatcher() is to generate a list of equations that best match by the given input
'''

def equationMatcher(N = 0):
	matched = []
	for func in equations:
		parameters = inspect.signature(func)
		parameterCount = 0
		matchedParameterCount = 0
		for param in parameters.parameters.values():
			if variables[str(param)] in inputs:
				#print(variables[str(param)])
				matchedParameterCount += 1
			parameterCount += 1
		#for N == 0 and N > 0, must first check if all of inputs match, then find functions that require more inputs
		if N == 0:
			if len(inputs) == matchedParameterCount and matchedParameterCount == parameterCount:
				matched.append(func)
		elif N > 0:
			if len(inputs) == matchedParameterCount and parameterCount - matchedParameterCount <= N:
				matched.append(func)
		#for N < 0, must first check if at least one input matches, check if all of the function's parameters matched,
		#then find functions that require less inputs
		else:
			if matchedParameterCount >= 1 and parameterCount - matchedParameterCount == 0 and len(inputs) - parameterCount <= abs(N):
				matched.append(func)
	return matched

#MAIN FUNCTION TO RUN THE EQUATION MATCHER ####################################################

def main():
	print(equationMatcher(-2))
	print(equationMatcher(-100))
	print(equationMatcher(0))
	print(equationMatcher(2))
	print(equationMatcher(100))

if __name__ == "__main__":
    main()
