import notion_functions as notion

# Get the path name to CSV file from the user
def getPathToCSV():
	print('Enter path to the Pluralsight .csv file: ')
	# TODO: get the path 
	file_path = ''
	return file_path

# Parse the data in the CSV file into a dictionary 
def parsePluralsightCSV():
	print()

# Convert the data into a Notion page
def convertToNotion():
	# Create new page
	page_response = notion.createPage('My New Page')
	if page_response == None:
		return
	page_response_data = page_response.json()	
	new_page_id = page_response_data['id']

	# TODO: Create new toggle header 3 for each module name

def main():
	file_path = getPathToCSV()
	data = parsePluralsightCSV()
	convertToNotion()

if __name__ == "__main__":
	main()