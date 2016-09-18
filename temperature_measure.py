def update_temperature_for_room(roomid):
	"""
	The temperature of the room.

	Params:
		roomid {str}: The ID of the room to be searched in the building API.

	Returns:
		{double}: The temperature of the room.
	"""

	response = http.get(URI_FOR_B11_WASP, params: {'Room': roomid})

	return response.Temperature