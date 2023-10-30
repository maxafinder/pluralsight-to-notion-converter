import os
import dotenv
import requests

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
def create_page(title):
	payload_data = {
			'parent': { 'page_id': notion_page_id },
			'properties': {
				'title': {
					'title': [
						{
							'text': {
								'content': title 
							}
						}
					]
				}
			}
	}
	response = send_notion_request('pages', payload_data)
	if response.status_code == 200:
		print('Page created successfully:', response.json())
		return response
	else:
		print('Failed to create page:', response.status_code, response.text)
		return None

# Create a toggle header 3
def create_toggle_header3(title, new_page_id):
	payload_data = {

	}
