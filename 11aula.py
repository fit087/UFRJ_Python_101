# 05/06/2015
# Aula Pratica 11

# Exc 1
def find_matrix(Matrix, searched_num):
	"""
		Fun¸c˜ao que dada uma matriz de inteiros de tamanho qualquer e um n´umero inteiro, conta e
		retorna quantas vezes aquele n´umero aparece na matriz.
		"""
	#m = Matrix[:]
	counter = 0
	for lista in Matrix:
		#while searched_num in lista:
		for elem in lista:
			if elem == searched_num:
				counter +=1
				print ("achou")
	return counter
	
# Exc 2
def transpose_matrix(matrix):
	"Gera e retorna a matriz transposta."
	#m_trans = matrix[:]
	m_old = len(matrix[0])
	n_old = len(matrix)
	m_trans = [[]] * m_old
	print ("m_trans", m_trans)
	i = 0
	for coluna in matrix:
		print ("coluna", coluna)
		#m_trans[:][i] = coluna
		m_trans[:][i] = coluna
		i += 1
	#	for elem in coluna: pass
	#m_trans[:][i]
	return m_trans
		
	
	
	



def main():
	# matrix = [[1,2,3]*3]
	#matrix = [[1,2,3]]*3
	matrix = [[1,2,3],[1,2,4],[1,5,3]]
	num = 3
	print ("matrix= ", matrix)
	matrix[0][0]=9
	print ("matrix= ", matrix)
	print("find_matrix(matrix, num)= ", find_matrix(matrix, num))
	print("transpose_matrix(matrix) = ", transpose_matrix(matrix))
	#pass

	
if __name__ == '__main__':
	main()