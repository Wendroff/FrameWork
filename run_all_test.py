#!/home/wzf/.conda/envs/env_wzf/bin/python
import unittest
import os
import datetime as dt

if __name__ == '__main__':
    test_dir = './test'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

    test_log_dir = os.path.join(os.path.pardir, 'test_log')
    # if not os.path.isdir(test_log_dir):
    #     os.makedirs(test_log_dir)
    # with open(os.path.join(os.path.pardir, 'test_log', 'test_{}.log'.format(dt.datetime.today().strftime("%Y%m%d%H%M%S"))), 'w') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(discover)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)