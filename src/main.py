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
import time
import shutil
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

#print(dir(Gtk.InputPurpose.DIGITS))

class Handler:

    def __init__(self):
        self.path = ""
        self.days_old = 5

    def on_main_window_destroy(self, *args):
        Gtk.main_quit()
        
    def on_clear_button_clicked(self, button):
        if self.path is not "":
            now = time.time()
            folder = self.path
            folders, files = self.get_files_and_folders(folder)
            
            for f in files:
                if os.stat(f).st_mtime < now - self.days_old * 86400:
                    os.remove(os.path.join(folder, f))

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
            
    def on_delete_screenshots_button_clicked(self, button):
        folder = GLib.get_home_dir() + '/Pictures'
        folders, files = self.get_files_and_folders(folder)
        
        for f in files:
            if "creenshot" in f:
                os.remove(f)
            
    def on_model_button_settings_clicked(self, button):
        builder = Gtk.Builder()
        builder.add_from_file("main.ui")
        window = builder.get_object("main_window")
        settings_dialog = Gtk.Dialog(parent=window)
        settings_dialog.set_default_size(150, 100)
        settings_dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK)
        
        main_box = Gtk.Box(spacing=6)
        main_box.set_orientation(Gtk.Orientation.VERTICAL)
        main_box.set_homogeneous(True)
        
        grid2 = Gtk.Grid()
        grid2.set_column_homogeneous(True)
        grid2.set_row_homogeneous(True)
        delete_files_label = Gtk.Label(label="Delete files older than (days old): ")
        delete_files_label.set_halign(Gtk.Align.END)
        grid2.attach(delete_files_label, 0, 1, 1, 1)
        delete_files_entry = Gtk.Entry()
        delete_files_entry.set_text(str(self.days_old))
        delete_files_entry.set_margin_start(6)
        delete_files_entry.set_halign(Gtk.Align.START)
        grid2.attach(delete_files_entry, 1, 1, 1, 1)
        main_box.add(grid2)

        box = settings_dialog.get_content_area()
        box.add(main_box)
        settings_dialog.show_all()
        
        response = settings_dialog.run()
        
        if response == Gtk.ResponseType.OK:
            try:
                int(delete_files_entry.get_text())
                self.days_old = delete_files_entry.get_text()
            except ValueError:
                self.days_old = 5
        elif response == Gtk.ResponseType.CANCEL:
            self.days_old = 5
            
        settings_dialog.destroy()

builder = Gtk.Builder()
builder.add_from_file("main.ui")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()


