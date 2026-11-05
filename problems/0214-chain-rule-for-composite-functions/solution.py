import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	n = len(functions)
	der = 1 #will be later multiplied by each derivative of chain rule
	for i in range(n-1, -1, -1): # iterate through functions backwards
		f = functions[i]
		# for each function, compute derivative at that layer and 
		# value for next layer, and update der and x
		match f:
			case "square":
				der*= 2*x
				x = x**2
			case "sin":
				der*=np.cos(x)
				x = np.sin(x)
			case "exp":
				der*=np.exp(x)
				x = np.exp(x)
			case "log":
				der*=1/(x)
				x=np.log(x)
	return der
