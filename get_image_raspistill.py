import os
from datetime import datetime, timezone, timedelta
from astral.sun import sun
from astral.geocoder import database, lookup

# Current time, not all in UTC
now = datetime.now(timezone.utc)

# Get dusk/dawn times
city = lookup('Seattle', database())
s = sun(city.observer, now)

# Extra time [hours]
et = 0

# If sunset > 24 hours ahead of current time, subtract a day (screwy because on UTC sunrise/sunset happen on different days
if (s['dusk'] - now).days >= 1:
	print('subtracting a day')
	s = sun(city.observer, now - timedelta(days=1))

if now >= (s['dawn'] - timedelta(hours=et)) and now <= (s['dusk'] + timedelta(hours=et)):	
	print('Daytime, time is {:s}, sunrise was {:s}, taking a picture'.format(now.strftime('%H:%M'),s['dawn'].strftime('%H:%M')))
	dstring = now.strftime('%y%m%d%H%M')
	fname = '/home/pi/Documents/pv01/pv01_{:s}.jpg'.format(dstring)
	fnamel = '/home/pi/Documents/pv01/pvl01_{:s}.jpg'.format(dstring)
	fnameh = '/home/pi/Documents/pv01/pvh01_{:s}.jpg'.format(dstring)
	str = 'raspistill -o {:s} -ex auto -vf -hf -w 2028 -h 1520 -q 75 -ev 0'.format(fname)
	os.system(str)
	str = 'raspistill -o {:s} -ex auto -vf -hf -w 2028 -h 1520 -q 75 -ev -6'.format(fnamel)
	os.system(str)
	str = 'raspistill -o {:s} -ex auto -vf -hf -w 2028 -h 1520 -q 75 -ev 6'.format(fnameh)
	os.system(str)
else:
	print('Nighttime, time is {:s}, sunset was {:s}, resting'.format(now.strftime('%Y-%m-%d %H:%M'),s['dusk'].strftime('%Y-%m-%d %H:%M')))
