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

import os, shutil
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GExiv2', '0.10')
from gi.repository import Gtk, Gio, GLib, GExiv2

from helpers import get_files_and_folders
from constants import folder_cleaner_constants as constants

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/folder-box.ui')
class FolderBox(Gtk.ListBox):

    __gtype_name__ = "_list_box"

    _folder_box_label = Gtk.Template.Child()

    i = 0

    def __init__(self, label, *args, **kwargs):
        super().__init__(**kwargs)

        self.label = label + '/'
        
        self.settings = Gio.Settings.new(constants['main_settings_path'])
        FolderBox.i += 1
        self.settings.set_int('count', FolderBox.i)

    @Gtk.Template.Callback()
    def on__sort_button_clicked(self, button):
        GExiv2.initialize()
        folders, files = get_files_and_folders(self.label)
        for f in files:
            try:
                photo = GExiv2.Metadata.new()
                photo.open_path(f)
                if photo.has_tag('Exif.Image.DateTime'):
                    tag = photo.get_tag_string('Exif.Image.DateTime')
                    filedate = tag[:10].replace(':', '')
                    correct_path = self.label + filedate
                    if os.path.isdir(correct_path):
                        GLib.spawn_async(['/usr/bin/mv', f, correct_path])
                    else:
                        GLib.spawn_async(['/usr/bin/mkdir', '-p', correct_path])
                        GLib.spawn_async(['/usr/bin/mv', f, correct_path])
                else:
                    print('cannot read Date in: ', f)
            except:
                #TODO add GLib.Error handler
                print('cannot read EXIF in: ', f)


    @Gtk.Template.Callback()
    def on__sort_files_clicked(self, button):
        folders, files = get_files_and_folders(self.label)
        for f in files:
            filename, file_extension = os.path.splitext(f)
            ext = file_extension[1:]
            if ext not in folders:
                GLib.spawn_async(['/usr/bin/mkdir', '-p', self.label + ext])
                GLib.spawn_async(['/usr/bin/mv', f,  self.label + ext])
                folders.append(self.label + ext)
            else:
                GLib.spawn_async(['/usr/bin/mv', f,  self.label + ext])


    @Gtk.Template.Callback()
    def on__open_folder_clicked(self, button):
        GLib.spawn_async(['/usr/bin/xdg-open', self.label])


    @Gtk.Template.Callback()
    def on__close_folder_clicked(self, button):
        FolderBox.i -= 1
        self.settings.set_int('count', FolderBox.i)
        self.destroy()