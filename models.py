from typing import List
from text import Text, InlineCode

class Note:
	def __init__(self, time, url, text):
		self.time = time
		self.url = url
		self.text = text

	def get_notion_api_format(self):
		return {
			'object': 'block',
			'type': 'paragraph',
			'paragraph': {
				'rich_text': [
					Text('This some text with some ').format_req(),
					InlineCode('code').format_req(),
					Text(' in it.').format_req()
				]
			}
		}


class Clip:
	def __init__(self, name):
		self.name = name
		self.notes: List[Note] = []
	
	def add_note(self, note):
		self.notes.append(note)

	def get_notion_api_format(self):
		return {
			'object': 'block',
			'type': 'heading_3',
			'heading_3': {
				'rich_text': [{
					'type': 'text',
					'text': {
						'content': self.name
					}
				}],
				'color': 'default',
			}
		}
		


class Module:
	def __init__(self, name):
		self.name = name
		self.clips: List[Clip] = []

	def add_clip(self, clip):
		self.clips.append(clip)

	def get_clip(self, name):
		for clip in self.clips:
			if clip.name == name:
				return clip
		return None

	def get_notion_api_format(self):
		clip_notes_notion_api_formatted = []
		for clip in self.clips:
			clip_notes_notion_api_formatted.append(clip.get_notion_api_format())
			for note in clip.notes:
				clip_notes_notion_api_formatted.append(note.get_notion_api_format())
		return {
			'object': 'block',
			'type': 'heading_3',
			'heading_3': {
				'rich_text': [{
					'type': 'text',
					'text': {
						'content': self.name
					}
				}],
				'color': 'default',
				'is_toggleable': True,
				'children': clip_notes_notion_api_formatted
			}
		}



class Course:
	def __init__(self, title):
		self.title = title
		self.modules: List[Module] = []

	def add_module(self, module):
		self.modules.append(module)

	def get_module(self, name):
		for module in self.modules:
			if module.name == name:
				return module
		return None

	def get_notion_api_format(self, notion_page_id):
		modules_notion_api_formatted = []
		for module in self.modules:
			modules_notion_api_formatted.append(module.get_notion_api_format())
		return {
			'parent': { 'page_id': notion_page_id },
			'properties': {
				'title': {
					'title': [
						{
							'text': {
								'content': self.title
							}
						}
					]
				}
			},
			'children': modules_notion_api_formatted
		}



class PluralsightData:
	def __init__(self):
		self.courses: List[Course] = []

	def add_course(self, course):
		self.courses.append(course)
	
	def get_course(self, title):
		for course in self.courses:
			if course.title == title:
				return course
		return None

	def add_new_note(self, note_text, course_title, module_name, clip_name, clip_time, clip_url):
		course = self.get_course(course_title) 
		if course == None:
			course = Course(course_title)
			self.add_course(course)
		module = course.get_module(module_name)
		if module == None:
			module = Module(module_name)
			course.add_module(module)
		clip = module.get_clip(clip_name)
		if clip == None:
			clip = Clip(clip_name)
			module.add_clip(clip)
		new_note = Note(clip_time, clip_url, note_text)
		clip.add_note(new_note)