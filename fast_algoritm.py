import numpy as np


def route_hesitation_index_fast(A):

    n = A.shape[0]
    C_num = np.zeros((n, n), dtype=int)
    C_distance = np.zeros((n, n), dtype=int)
    i = 1
    mask = ~np.eye(n, dtype=bool)          

    while np.any(C_num[mask] == 0):

        G_i = np.linalg.matrix_power(A, i)  
        np.fill_diagonal(G_i, 0)            
        T = (C_num == 0) & mask             
        G_temp = T * G_i                    

        if np.sum(G_temp) == 0:
            break                           

        C_num += G_temp
        C_distance += (G_temp != 0) * i    
        i += 1
    return C_num, C_distance



# An example:
# G = [[0, 1, 1, 1, 1],
#      [1, 0, 0, 1, 1],
#      [1, 0, 0, 1, 1],
#      [1, 1, 1, 0, 1],
#      [1, 1, 1, 1, 0]]
#
# G = np.array(G)
# C_num, C_distance = route_hesitation_index_fast(G)
