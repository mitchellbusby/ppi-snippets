#This integer should be zero indexed
current_page_position = 0

def update_pagination(is_turned, direction, total_pages):
	"""
	The sensitivity of the encoder will depend on how often this is called, and the turn period. Returns the updated scroll position.
	----
	Params:
	is_turned {int}: A boolean integer determining whether or not the encoder is being turned currently.

	direction {int}: A boolean integer determining whether or not the encoder 
					is being turned clockwise or counterclockwise. 1 indicates clockwise, otherwise counter.
	total_pages {int}: Total number of pages
	---
	Returns:
		{int} The absolute page to paginate to.
	"""

	#Dictates how often pagination should occur; a value of 1 = once per cycle 
	#if the scroll wheel is turned.
	TURN_PERIOD = 1


	if is_turned == 1:
		if direction == 1:
			current_page_position += TURN_PERIOD
		else:
			current_page_position -= TURN_PERIOD

	#Wraparound to first page
	if current_page_position >= total_pages:
		current_page_position = 0

	#Wraparound to last page
	if current_page_position  < 0:
		current_page_position = total_pages - 1

	return round(current_page_position)