"""
util.py
A file containing utility functions.

"""

def title_case(sentence):
	"""
	Convert a string into title case.

	Title case means that the first letter of each word is capitalized with all
	other letter lower case.

	Parameters
	----------
	sentence : str
		String to be converted into title case.

	Returns
	-------
	title : str
		String in title case format.

	Example
	-------
	>>> title_case("ThiS iS a StriNg tO be conVerTed")
	'This Is A String To Be Converted'
	"""
	words = sentence.split()
	title = ""
	for word in words:
		title = title + word[0].upper() + word[1:].lower() + " "
	return title
