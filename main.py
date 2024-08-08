import numpy as np

num = "FFFAEDA10"

h = int(num,16)
hep = np.base_repr(h, base=7)

print("\nConversor de bases")

print('{} em Binario:{}'.format(num, bin(h)[2:]))
print('{} em octal:{}'.format(num, oct(h)[2:]))
print('{} em heptadecimal:{}'.format(num, (hep)))

print("\nSVD")

A = np.matrix([[3, 2, 7],[2, 5, 7],[7, 1, 8]])
autov_A = np.linalg.eig(A)
print('AutoValores:{}\n'.format(autov_A[0]))

print('AutoVetor:{}\n'.format(autov_A[1]))

U, S, Vt = np.linalg.svd(A, full_matrices=True)
S = np.diag(S)

print('Matriz de valores singulares:{}\n'.format(S))

print('Matriz de valores singulares a esquerda:{}\n'.format(U))

print('Matriz de valores singulares a direita:{}'.format(Vt))

U, S, Vt = np.linalg.svd(A, full_matrices=True)

print('\nValores singulares:', np.round(S, 4))