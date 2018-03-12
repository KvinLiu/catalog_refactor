import sys

sys.path.insert(0, '/home/grader/project/catalog')

activate_this = '/home/grader/project/catalog/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from run import app as application