import os
import time

N = 24*60

for i in range(N):
   fname = 'pic_{:07d}.jpg'.format(i)
   str = 'raspistill -o {:s} -ex auto -q 75 -w 1024 -h 768'.format(fname)
   os.system(str)
   time.sleep(60)


