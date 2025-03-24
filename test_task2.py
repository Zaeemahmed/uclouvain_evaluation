import unittest
from task2 import reachable
from task1 import mat_to_list

class TestReachableNodes(unittest.TestCase):
    def test_reachable_nodes(self):
        adj_mat = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0]
        ]
        adj_list = mat_to_list(adj_mat)
        self.assertEqual(reachable(adj_list, 0), {0, 1, 2, 3, 4})

if __name__ == '__main__':
    unittest.main()
