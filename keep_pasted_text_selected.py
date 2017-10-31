

import sublime
import sublime_plugin


class SampleListener(sublime_plugin.EventListener):

    def on_text_command(self, view, command, args):
        # print ("About to execute " + command)

        if command == "paste_and_indent":
            self.start_selection = []

            for selection in view.sel():
                self.start_selection.append( selection.begin() )

    def on_post_text_command(self, view, command, args):
        # print ("Finished executing " + command)

        if command == "paste_and_indent":
            index = -1

            selections        = view.sel()
            selections_count  = len( self.start_selection )
            regions_to_create = []

            for selection in selections:
                index += 1

                if index < selections_count:
                    regions_to_create.append( sublime.Region( self.start_selection[index], selection.end() ) )

            for region in regions_to_create:
                selections.add( region )

