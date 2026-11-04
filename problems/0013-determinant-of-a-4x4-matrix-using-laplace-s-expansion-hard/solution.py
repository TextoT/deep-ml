
def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	n = len(matrix)
	if n == 1:
		return matrix[0][0]
	else: #expand along first column
		ans = 0
		m = 1
		for i in range(n):
			submatrix = [row[1:] for row in matrix]
			submatrix.pop(i)
			ans += matrix[i][0] * m * determinant_4x4(submatrix)
			m *= -1
		return ans