import sys
from os.path import abspath
from os.path import dirname as d

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
