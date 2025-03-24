import unittest
from task1 import mat_to_list

class TestAdjacencyMatrixToList(unittest.TestCase):
    def test_adjacency_matrix_to_list(self):
        adj_mat = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0]
        ]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(adj_list, [[1], [0, 2], [1, 3], [2, 4], [3]])

if __name__ == '__main__':
    unittest.main()