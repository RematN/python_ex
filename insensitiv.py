#initial list
classrooms=['Toy','class2','CLASS3','class4','class5']

# class to be searched
class_room='toy'

#' claß3' means 'class3'

#function to search item
def search_classroom():
	for classes in classrooms:
		if class_room.casefold()==classes.casefold():
			return True

	else:
		return False

if search_classroom():

# If function returns true
	print('Classroom you are searching is present')

else:

# If function returns false
	print('Classroom you are searching is not present')
