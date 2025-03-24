import unittest

def run_tests():
    # Load all tests from the tests directory
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('')

    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

if __name__ == '__main__':
    run_tests()

