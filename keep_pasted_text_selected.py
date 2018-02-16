

import sublime
import sublime_plugin


class SampleListener(sublime_plugin.EventListener):

    def __init__(self):
        super().__init__()
        self.start_selection = []

    def on_text_command(self, view, command, args):
        # print ("About to execute " + command)

        if command == "paste_and_indent":
            self.start_selection.clear()

            for selection in view.sel():
                self.start_selection.append( selection.begin() )

    def on_post_text_command(self, view, command, args):
        # print ("Finished executing " + command)

        if command == "paste_and_indent":
            index = -1
            selections = view.sel()

            selection_offset  = 0
            selections_count  = len( self.start_selection )
            regions_to_create = []

            for selection in selections:
                index += 1

                if index < selections_count:
                    selected_region = sublime.Region( selection_offset + self.start_selection[index], selection.end() )
                    regions_to_create.append( selected_region )

                selection_offset = selection.end() - self.start_selection[index]
                # print( "selection_offset:", selection_offset )

            for region in regions_to_create:
                selections.add( region )

