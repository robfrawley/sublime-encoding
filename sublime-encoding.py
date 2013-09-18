import sublime
import sublime_plugin

class ShowFileEncodingCommand(sublime_plugin.WindowCommand):
    def run(self):
    	sublime.message_dialog('Current file and encoding: '+self.window.active_view().encoding())
        return