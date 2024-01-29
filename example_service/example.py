import argparse
import datetime as dt
import time

from astropy.io import fits
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('-msg', help='Message you want to display')

if  __name__ == "__main__":
    args = parser.parse_args()
    msg = args.msg
    while True:
        current_time = dt.datetime.now()
        print(f'Current Time: {current_time:%b %d, %Y %H:%M:%S}\n{msg}')
        time.sleep(2)