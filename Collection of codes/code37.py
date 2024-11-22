def add_matrices(mat1, mat2):
  if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
    return 'Matrices must have the same dimension for addition'
  
  result = []
  
  for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[0])):
      row.append(mat1[i][j] + mat2[i][j])
    result.append(row)
  return result

matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,2,3], [4,5,6], [7,8,9]]

result_matrices = add_matrices(matrix1, matrix2)

if isinstance(result_matrices, str):
  print(result_matrices)
else:
  print('Sum of Matrices:')
  for row in result_matrices:
    print(row)