import re
import sublime, sublime_plugin

class ControlScrollCommand(sublime_plugin.TextCommand):
	''' cool Wheeler. 
	Simple command to chage digits or lists by mouse wheel
	On future: file-types'''
	def run(self, edit, down=False):
		settings = sublime.load_settings('controlscroll.sublime-settings')
		jump = settings.get('jump', 1000)
		position = self.view.viewport_position()
		self.view.set_viewport_position((position[0], position[1] + (jump if down else -jump)), True);