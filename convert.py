from typing import List
import csv
import notion_functions as notion
from models import PluralsightData 
from text import parse_text

# Parse the data in the CSV file into a dictionary 
def parse_pluralsight_csv(file_path):
	csvfile = open(file_path, 'r')
	csvreader = csv.reader(csvfile)
	next(csvreader)
	pluralsight_data = PluralsightData()
	for row in csvreader:
		pluralsight_data.add_new_note(note_text=row[0], course_title=row[1], module_name=row[2], clip_name=row[3], clip_time=row[4], clip_url=row[5])
	return pluralsight_data


# Convert the data into a Notion page
def convert_to_notion(pluralsight_data: PluralsightData):
	for course in pluralsight_data.courses:
		notion.create_page(course) 


def main():
	file_path = str(input('Enter full path name to Pluralsight notes (.csv): '))
	pluralsight_data = parse_pluralsight_csv(file_path)
	convert_to_notion(pluralsight_data)

my_str = """YAML syntax:
1. YAML files are composed of Maps and Lists. All of these things can be nested inside each other.
2. Indentation matters.
3. Always use spaces instead of tabs.
4. Maps are `name: value` pairs.
5. Lists are a sequence of items that use the `-` character.
"""

if __name__ == "__main__":
	main()
