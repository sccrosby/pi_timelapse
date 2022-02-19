import os
from datetime import datetime

now = datetime.now()
dstring = now.strftime('%y%m%d%H%M')
fname = '../pv01/pv01_{:s}.jpg'.format(dstring)
str = 'raspistill -o {:s} -ex auto -q 75 -w 1024 -h 768'.format(fname)
os.system(str)


