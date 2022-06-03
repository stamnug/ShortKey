import sublime
import sublime_plugin
import subprocess


def copy2clip(txt):
    cmd = f'echo|set /p="{txt.strip()}"|clip'
    return subprocess.check_call(cmd, shell=True)

class GetPathCommand(sublime_plugin.WindowCommand):
	def run(self):
		path = self.window.extract_variables()['file_path']
		self.window.active_view().set_status('path','❤  ' + path + '  💜')
		
		copy2clip(path)


