def filter_rooms(rooms, potentiometerValue):
	"""
	Params:
		rooms {List<Room>}: all Rooms in the building, where a Room has a people_count attribute.
		potentiometerValue {int}: an integer between 0-1023 that needs to be mapped.
	Returns:
		{List<Room>}: The list of rooms that match the mapped people threshold.
	"""
	
	people_threshold = 0

	if potentiometerValue < 250:
		people_threshold = 2
	else if potentiometerValue < 500:
		people_threshold = 7
	else if potentiometerValue < 750:
		people_threshold = 15
	else if potentiometerValue < 1000:
		people_threshold = 20
	else:
		#Dummy value to make sure all rooms are shown
		people_threshold = 1000

	#Filters  down to only rooms that match the people threshold
	return filter(lambda x: x.people_count <= people_threshold, rooms)