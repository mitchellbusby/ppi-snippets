#TIME_ELAPSED_SINCE_LAST_CALL_TO_THIS_METHOD should be relative
#to the number of times that manage_device_wake is called per second.


def manage_device_wake(is_awake, time_since_last_user_input):
	"""
	Manages the device wake
	Params:
		is_awake {bool}: Whether the device is currently awake.
		time_since_last_user_input {int}: seconds since the user last interacted with the device

	"""

	if is_awake:
		#Check if it should be turned off, triggers after 30 seconds
		if time_since_last_user_input > 30:
			is_awake = False
	else:
		check_to_wake_device()

def check_to_wake_device():
	"""
	Checks whether to wake the device and then sets is_awake to true
	"""
	if to_wake_device(measure_proximity()):
		is_awake = True


def to_wake_device(proximity, interval=0):
	"""
	Determines whether to wake the device up.
	Params:
		proximity {double}: The current proximity to the user in centimetres
		interval {integer}: milliseconds since the trigger proximity was first reached.
	"""

	#Deal in centimetres
	TRIGGER_PROXIMITY = 50

	#Will wake after two seconds of being in TRIGGER_PROXIMITY
	INTERVAL_WAKE_TRIGGER = 2000

	#Measure every 300 milliseconds
	TIME_ELAPSED_SINCE_LAST_CALL_TO_THIS_METHOD = 300

	if (proximity > 50):
		interval += TIME_ELAPSED_SINCE_LAST_CALL_TO_THIS_METHOD
		if interval > INTERVAL_WAKE_TRIGGER:
			return True
	return False

def measure_proximity():
	"""TODO"""