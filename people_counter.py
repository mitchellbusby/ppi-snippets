def update_people_count_for_room(roomid):
	"""
	The number of people in the room at any one time.

	Params:
		roomid {str}: The ID of the room to be searched in the building API.

	Returns:
		{int}: The number of people.
	"""

	response = http.get(URI_FOR_PEOPLE_COUNTER, params: {'Room': roomid})

	return response.PeopleCount