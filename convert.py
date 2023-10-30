import csv
import notion_functions as notion
from models import Courses, Course, Module, Clip, Note

# Parse the data in the CSV file into a dictionary 
def parse_pluralsight_csv(file_path):
	csvfile = open(file_path, 'r')
	csvreader = csv.reader(csvfile)
	next(csvreader)

	courses = Courses()
	for row in csvreader:
		courses.add_new_note(note_text=row[0], course_title=row[1], module_name=row[2], clip_name=row[3], clip_time=row[4], clip_url=row[5])
	print(courses)

# Convert the data into a Notion page
def convert_to_notion(pluralsight_data):
	# Create new page
	page_response = notion.create_page('My New Page')
	if page_response == None:
		return
	page_response_data = page_response.json()	
	new_page_id = page_response_data['id']

	# TODO: Create new toggle header 3 for each module name


def main():
	file_path = str(input('Enter full path name to Pluralsight notes (.csv): '))
	pluralsight_data = parse_pluralsight_csv(file_path)
	#convert_to_notion(pluralsight_data)

if __name__ == "__main__":
	main()