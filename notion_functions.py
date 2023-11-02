import os
import dotenv
import requests
from models import Course


# Load environment variables
dotenv.load_dotenv()
notion_key = os.environ['NOTION_KEY']
notion_page_id = os.environ['NOTION_PAGE_ID']

	
# Send a request to the Notion API
def send_notion_request(endpoint, payload_data):
	headers = {
			'Authorization': f'Bearer {notion_key}',
			'Content-Type': 'application/json',
			'Notion-Version': '2022-06-28'
	}
	response = requests.post(f'https://api.notion.com/v1/{endpoint}', headers=headers, json=payload_data)
	return response


# Create a new Notion page
def create_page(course: Course):
	payload_data = course.get_notion_api_format(notion_page_id)
	response = send_notion_request('pages', payload_data)
	if response.status_code == 200:
		print('Page created successfully:', response.json())
	else:
		print('Failed to create page:', response.status_code, response.text)
