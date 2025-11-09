# Shortest Path Algorithm
A fast algorithm that can simultaneously calculate the number and length of the shortest paths between all pairs of nodes in a network. Both MATLAB and Python versions of the code are provided.

## Abstract:
Complex networks describe a broad range of systems in nature and society. As a fundamental concept of graph theory, the path connecting nodes and edges plays a crucial role in network science, where the computation of shortest path lengths and numbers has garnered substantial focus. It is well known that powers of the adjacency matrix can calculate the number of walks, specifying their corresponding lengths. However, developing methodologies to quantify both the number and length of shortest paths through the adjacency matrix remains a challenge. Here, we extend powers of the adjacency matrix from walks to shortest paths. We address the all-pairs shortest path count problem and propose a fast algorithm based on powers of the adjacency matrix that counts both the number and the length of all shortest paths. Numerous experiments on synthetic and real-world networks demonstrate that our algorithm is significantly faster than the classical algorithms across various network types and sizes. Moreover, we verified that the time complexity of our proposed algorithm significantly surpasses that of the current state-of-the-art algorithms. The superior property of the algorithm allows for rapid calculation of all shortest paths within large-scale networks, offering significant potential applications in traffic flow optimization and social network analysis.


## Reference:
If you find this algorithm helpful, please cite：

"Tan D, Deng Y, Xiao Y, et al. Shortest path counting in complex networks based on powers of the adjacency matrix[J]. Chaos: An Interdisciplinary Journal of Nonlinear Science, 2024, 34(10): 101104 ."
