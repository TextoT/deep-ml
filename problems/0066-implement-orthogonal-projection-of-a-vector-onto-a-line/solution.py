
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	c = (sum([v[i]*L[i] for i in range(len(v))]))/(sum([L[i]*L[i] for i in range(len(v))]))
	return [c*L[i] for i in range(len(L))]
