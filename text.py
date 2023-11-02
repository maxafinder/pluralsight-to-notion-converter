import re
from typing import List
from abc import abstractmethod, ABC

class ContentType(ABC):
	@abstractmethod
	def format_req(self):
		pass

class Text(ContentType):
	def __init__(self, text: str):
		self.text = text

	def format_req(self):
		return {
			'type': 'text',
			'text': {
				'content': self.text
			}
		}


class InlineCode(ContentType):
	def __init__(self, text: str):
		self.text = text

	def format_req(self):
		return {
			'type': 'text',
			'text': {
				'content': self.text
			},
			'annotations': {
				'code': True
			}
		}


class CodeBlock(ContentType):
	def __init__(self, text: str):
		self.text = text.strip('\n')
	
	def format_req(self):
		return {
			'type': 'code',
			'code': {
				'rich_text': [{
					'type': 'text',
					'text': {
						'content': self.text
					}
				}],
				'language': 'plain text'
			}
		}


class NumberedList(ContentType):
	def __init__(self, items):
		self.items = items

	def format_req(self):
		numbered_list_notion_api_formatted = []
		for item in self.items:
			numbered_list_notion_api_formatted.append(self.__format_item(item))
		return numbered_list_notion_api_formatted

	def __format_item(self, item: str):
		return {
			'type': 'numbered_list_item',
			'numbered_list_item': {
				'rich_text': [
					{
						'type': 'text',
						'text': {
							'content': item,
						}
					}
				],
			}
		}


def parse_text(text) -> List[ContentType]:
	parts = []
	text_part = ''
	i = 0
	while i < len(text):
		if (numbered_list_part := is_numbered_list(text[i:])):
			if text_part != '':
				parts.append(Text(text_part))
				text_part = ''
			parts.append(NumberedList(numbered_list_part))
			i += get_numbered_list_char_count(numbered_list_part)
		elif (code_block_part := is_code_block(text[i:])):
			if text_part != '':
				parts.append(Text(text_part))
				text_part = ''
			parts.append(CodeBlock(code_block_part))
			i += len(code_block_part) + 6
		elif (inline_code_part := is_inline_code(text[i:])):
			if text_part != '':
				parts.append(Text(text_part))
				text_part = ''
			parts.append(InlineCode(inline_code_part))
			i += len(inline_code_part) + 2
		else:
			text_part += text[i]
			i += 1
	if text_part != '':
		parts.append(Text(text_part))
	return parts		

# If the text starts with a code block part, return its content
def is_code_block(text):
	pattern = r"^```(.*?)```"
	match = re.search(pattern, text, re.DOTALL)
	if match:
		return match.group(1)
	else:
		return None

# If the text starts with an inline code part, return its content
def is_inline_code(text):
	pattern = r"^`(.+?)`"
	match = re.search(pattern, text, re.DOTALL)
	if match:
		return match.group(1)
	else:
		return None

# If the text starts with a numbered list part, return its content
def is_numbered_list(text):
	list_match = re.search(r'^(1\..*?)(?=\n(?!\d+\. )|$)', text, re.DOTALL)
	if not list_match:
			return []
	# Split the captured list into items.
	items = re.split(r'\n\d+\. ', list_match.group(1))
	# The first item will have the "1. " prefix, so we remove it.
	items[0] = items[0][3:]
	return items

# Return the original number of character that were in this numbered list
def get_numbered_list_char_count(numbered_list):
	count = 0 
	for item in numbered_list:
		count += len(item) + 4 # 3 for num-dot-space and 1 for ending '\n'
	return count
