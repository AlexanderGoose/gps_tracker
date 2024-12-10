import gpsd
import time
import json
import datetime

# connect to local device
gpsd.connect()

# get gps position
# packet = gpsd.get_current()

# create path name using time to differentiate
t = datetime.datetime.now()
path = f'gps_data_{t.strftime("%Y-%m-%d_%H:%M:%S")}.json'

data = []

for i in range(5):
	# let sleep in between calls
	time.sleep(10)

	# get gps position
	packet = gpsd.get_current()

	t = datetime.datetime.now()
	print(f'Time: {t.strftime("%H:%M:%S")}')
	print(f'Lon: {packet.lon}')
	print(f'Lat: {packet.lat}')
	print(f'Alt: {packet.alt}')
	# time.sleep(5)
	print('\n')

	# add the data to the dict
	curr_data = {
		'Lon': packet.lon,
        	'Lat': packet.lat,
        	'Alt': packet.alt
	}
	data.append(curr_data)

	# add the dict to a json file
	with open(path, 'w') as file:
		json.dump(data, file, indent=4)
