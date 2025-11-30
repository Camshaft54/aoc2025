import shutil
import os
import sys

day = sys.argv[1]
shutil.copytree('template', f'day{day}')
os.rename(f'day{day}/template.py', f'day{day}/day{day}.py')