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
gi.require_version('GExiv2', '0.10')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Gio, GLib, Notify, GExiv2

from helpers import get_files_and_folders, operations, folders_made, labels
from constants import folder_cleaner_constants as constants

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/folder-box.ui')
class FolderBox(Gtk.ListBox):

    __gtype_name__ = "_list_box"

    _folder_box_label = Gtk.Template.Child()

    i = 0

    def __init__(self, label, *args, **kwargs):
        super().__init__(**kwargs)

        self.label = label + '/'

        #TODO
        labels.append(self.label[:-1])

        Notify.init('com.github.Latesil.folder-cleaner')
        
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
                if photo.has_exif() and photo.has_tag('Exif.Image.DateTime'):
                    tag = photo.get_tag_string('Exif.Image.DateTime')
                    filedate = tag[:10].replace(':', '')
                    folder_for_photo = self.label + filedate

                    #Gio.Files
                    photo_file = Gio.File.new_for_path(f)
                    destination_folder = Gio.File.new_for_path(folder_for_photo)
                    destination_for_photo = Gio.File.new_for_path(folder_for_photo + '/' + photo_file.get_basename())

                    if GLib.file_test(folder_for_photo, GLib.FileTest.IS_DIR):
                        photo_file.move(destination_for_photo, Gio.FileCopyFlags.NONE)
                    else:
                        Gio.File.make_directory(destination_folder)
                        photo_file.move(destination_for_photo, Gio.FileCopyFlags.NONE)
                else:
                    print('cannot read data in:', f)
            except GLib.Error as err:
                print('%s: %s in file: %s, (code: %s)' % (err.domain, err.message, f, err.code))
        
        notification = Notify.Notification.new('Folder Cleaner', "All photos were successfully sorted")
        notification.show()


    @Gtk.Template.Callback()
    def on__sort_files_clicked(self, button):
        folders, files = get_files_and_folders(self.label, absolute_folders_paths=False)
        for f in files:
            content_type, val = Gio.content_type_guess(f)
            simple_file = Gio.File.new_for_path(f)
            name, ext = simple_file.get_basename().rsplit('.', 1)

            if self.settings.get_boolean('sort-by-category'):
                destination_folder = Gio.File.new_for_path(self.label + '/' + content_type.split('/')[0].capitalize())
            else:
                destination_folder = Gio.File.new_for_path(self.label + '/' + ext)
            destination_path = destination_folder.get_path() + '/' + simple_file.get_basename()
            destination_for_files = Gio.File.new_for_path(destination_path)

            if ext not in folders:
                Gio.File.make_directory(destination_folder)
                folders_made.append(destination_folder.get_path())
                simple_file.move(destination_for_files, Gio.FileCopyFlags.NONE)
                folders.append(ext)
                operations[f] = destination_path
            else:
                simple_file.move(destination_for_files, Gio.FileCopyFlags.NONE)
                operations[f] = destination_path

        self.settings.set_boolean('is-sorted', True)


    @Gtk.Template.Callback()
    def on__open_folder_clicked(self, button):
        GLib.spawn_async(['/usr/bin/xdg-open', self.label])


    @Gtk.Template.Callback()
    def on__close_folder_clicked(self, button):
        FolderBox.i -= 1

        #TODO
        labels.remove(self.label[:-1])
        
        self.settings.set_int('count', FolderBox.i)
        self.destroy()