class Text:
	def __init__(self, text):
		self.text = text

	def format_req(self):
		return {
			'type': 'text',
			'text': {
				'content': self.text
			}
		}

class InlineCode:
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

class CodeBlock:
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

class NumberedList:
	def __init__(self):
		self.items = []

	def add_item(self, item: NumberedListItem):
		self.items.append(item)

class Content:
	def __init__(self, text):
		self.text = text
		self.content = parse_text(text)

def parse_text(text):
	parts = []
	for i in range(0, len(text)):
		if text[i] == '`':
			if (i + 2) < len(text) and text[i + 1] == '`' and text[i + 2] == '`':
				print('new code block')
			else:
				print('new inline code')
		if (i + 2) < len(text) and text[i] == '1' and text[i + 1] == '.' and text[i + 2] == ' ':
			print('starting numbered list')


