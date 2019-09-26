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

	
import subprocess
import os
import shutil
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

print(dir(shutil))

class Handler:

    def __init__(self):
        self.path = ""

    def on_main_window_destroy(self, *args):
        Gtk.main_quit()

    def on_model_button_add_clicked(self, button):
        print("on_model_button_add_clicked!")
        
    def on_model_button_about_clicked(self, button):
        about = Gtk.AboutDialog()
        about.set_program_name("Folder Cleaner")
        about.set_version("0.0.1")
        about.set_authors(["Letalis"])
        about.set_artists(["Late"])
        about.set_copyright("🄯 Copylefted")
        about.set_comments("Program for sorting and cleaning in file-trash folders")
        about.set_website("https://gitlab.com/Latesil/folder-cleaner")
        about.set_website_label("Website")
        about.set_wrap_license(True)
        about.set_license_type(Gtk.License.GPL_3_0)
        about.run()
        about.destroy()
        
    def on_main_button_folder_file_set(self, button):
        self.path = button.get_filename()
        
    def get_files_and_folders(self, folder):
        folder_list = []
        files_list = []
    
        for root, dirs, filenames in os.walk(folder):
            for dirname in dirs:
                folder_list.append(os.path.abspath(os.path.join(root, dirname)))
                
            for filename in filenames:
                files_list.append(os.path.abspath(os.path.join(root, filename)))
                
            break
         
        return folder_list, files_list
        
    def on_main_button_sort_clicked(self, button):
        if self.path is not "":
            folder = self.path
            folders, files = self.get_files_and_folders(folder)
            
            for f in files:
                filename, file_extension = os.path.splitext(f)
                ext = file_extension[1:]
                if ext not in folders:
                    subprocess.call(['mkdir', '-p', self.path + '/' + ext])
                    shutil.move(f, self.path + '/' + ext)
                    folders.append(self.path + '/' + ext)
                else:
                    shutil.move(f, self.path + '/' + ext)
        
    def on_main_button_open_clicked(self, button):
        if self.path is not "":
            subprocess.call(['xdg-open', self.path])
        else:
            pass
            
    def on_model_button_settings_clicked(self, button):
        print("on_model_button_settings_clicked")



builder = Gtk.Builder()
builder.add_from_file("main.ui")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()


