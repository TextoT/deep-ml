import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	g = np.array(gradient)
	magnitude = np.sqrt(np.sum(g**2))
	if magnitude == 0: # edge case of 0 magnitude
		direction = g
	else:
		direction = g/magnitude # normalized version
	return {"magnitude": magnitude,"direction": direction, "descent_direction": -direction}
