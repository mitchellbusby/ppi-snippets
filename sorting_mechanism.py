sort_method = none

def check_sorting_method(buttonState):
	"""
	Checks if the button is pressed, and if so change the sorting mechanism
	Params:
		buttonState {enum: HIGH, LOW}: the current button state
	"""
	if buttonState == HIGH:
		#Change sort method
		if sort_method = BY_PEOPLE:
			sort_method = BY_TIME_FREE
		else:
			sort_method = BY_PEOPLE