import sublime
import sublime_plugin
import os

class FileCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel('File Path:', '', self.on_done, None, None)

	def on_done(self, filepath):
		dirname = os.path.dirname(filepath)
		filename = os.path.basename(filepath)

		dirpath = self.window.extract_variables()['file_path']
		if dirname:
			dirpath += f"\\{dirname}"
			os.makedirs(f"{dirpath}")
		
		if not os.path.isfile(f"{dirpath}\\{filename}"): 
			file = open(f"{dirpath}\\{filename}", 'w')
			file.close()

		view = self.window.open_file(f"{dirpath}\\{filename}")
		self.window.active_view().set_status('path','❤  ' + dirpath + '  💜')