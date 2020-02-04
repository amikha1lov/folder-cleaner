#!/usr/bin/python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

from folder_box import FolderBox
from preferences import PreferencesWindow
from constants import folder_cleaner_constants as constants

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/folder-cleaner.ui')
class FolderCleaner(Gtk.ApplicationWindow):

    __gtype_name__ = "_main_window"

    _about_window = Gtk.Template.Child()
    _add_label = Gtk.Template.Child()
    _main_list_box_row = Gtk.Template.Child()
    _main_list_box = Gtk.Template.Child()

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, title="Folder Cleaner", application=app)

        self.set_wmclass("Folder Cleaner", "Folder Cleaner")
        self.settings = Gio.Settings.new(constants['main_settings_path'])
        self.settings.connect("changed::count", self.on_count_change, None)


    @Gtk.Template.Callback()
    def on__add_button_clicked(self, button):
        chooser = Gtk.FileChooserDialog(title="Open Folder",
                                        transient_for=self,
                                        action=Gtk.FileChooserAction.SELECT_FOLDER,
                                        buttons=("Cancel", Gtk.ResponseType.CANCEL,
                                                 "OK", Gtk.ResponseType.OK))
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            label = chooser.get_filename()
            folder = FolderBox(label)
            folder._folder_box_label.set_label(label)
            self._main_list_box.insert(folder, -1)
            chooser.destroy()
        else:
            chooser.destroy()

    @Gtk.Template.Callback()
    def on__preferences_button_clicked(self, button):
        preferences = PreferencesWindow(self)
        preferences.set_transient_for(self)
        preferences.run()
        preferences.destroy()

    @Gtk.Template.Callback()
    def on__about_button_clicked(self, button):
        about = self._about_window
        about.run()
        about.destroy()

    def on_count_change(self, settings, key, button):
        if self.settings.get_int('count') > 0:
            self._main_list_box_row.set_visible(False)
        else:
            self._main_list_box_row.set_visible(True)
