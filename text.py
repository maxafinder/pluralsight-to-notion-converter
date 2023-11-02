import re
from typing import List
from abc import abstractmethod, ABC

class ContentType(ABC):
	@abstractmethod
	def format_req(self):
		pass

class Text(ContentType):
	def __init__(self, text):
		self.text = text

	def format_req(self):
		return {
			'type': 'text',
			'text': {
				'content': self.text
			}
		}


class InlineCode(ContentType):
	def __init__(self, text):
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
	def __init__(self, text):
		self.text = text
	
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


class NumberedListItem:
	def __init__(self, number, content):
		self.number = number
		self.content = content


class NumberedList(ContentType):
	def __init__(self):
		self.items = []

	def add_item(self, item: NumberedListItem):
		self.items.append(item)
	
	def format_req(self):
		pass


def parse_text(text) -> List[ContentType]:
	parts = []
	text_part = ''
	#for i in range(0, len(text)):
	i = 0
	while i < len(text):
		if (code_block_part := is_code_block(text[i:])):
			if text_part != '':
				parts.append(Text(text_part))
				text_part = ''
			#parts.append(CodeBlock(code_block_part))
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

def is_numbered_list_start(text, i):
	return (i + 3) < len(text) and text[i:4] == '\n1. '

# TODO: parse numbered list	
def parse_numbered_list(text):
	print()
