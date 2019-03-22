import os
import time
import sys
import platform
from datetime import datetime
"""
Simple daemon
"""


def looper():
    """
    Continuously looping function
    :return:
    """

    while True:

        # read possible environment variables
        var_1 = os.getenv('VAR_1')
        var_2 = os.getenv('VAR_2')
        var_3 = os.getenv('VAR_3')
        var_4 = os.getenv('VAR_4')

        # print environment variables and python info to stdout
        print(f"Environment variables: VAR_1: {var_1}, VAR_2: {var_2}, VAR_3: {var_3}, VAR_4: {var_4}")
        print(f"python details: {platform.python_version()} now: {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}")

        # sleep for one second
        time.sleep(1)


if __name__ == "__main__":
    # check python version and exit if it is wrong
    if sys.version_info[0] != 3 or sys.version_info[1] < 7:
        raise Exception("Must be using Python 3.7.X  not {}.{}".format(sys.version_info[0], sys.version_info[1]))
    sys.exit(looper())
