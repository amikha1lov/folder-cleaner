import os, shutil
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib

from helpers import get_files_and_folders

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/folder-box.ui')
class FolderBox(Gtk.ListBox):

    __gtype_name__ = "_list_box"

    _folder_box_label = Gtk.Template.Child()

    i = 0

    def __init__(self, label, *args, **kwargs):
        super().__init__(**kwargs)

        self.label = label + '/'
        
        self.settings = Gio.Settings.new('com.github.Latesil.folder-cleaner')
        FolderBox.i += 1
        self.settings.set_int('count', FolderBox.i)

    @Gtk.Template.Callback()
    def on__sort_button_clicked(self, button):
        #find better solution
        for (dirpath, dirnames, filenames) in os.walk(self.label):
            for f in filenames:
                filedate = f[4:12]
                correct_path = self.label + filedate
                abs_filename = self.label + f
                if os.path.isdir(correct_path):
                    shutil.move(abs_filename, correct_path)
                else:
                    os.mkdir(correct_path)
                    shutil.move(abs_filename, correct_path)
            break


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