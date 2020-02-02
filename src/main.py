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
import os, sys
import time
import shutil
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

#print(dir(Gtk.InputPurpose.DIGITS))
from window import FolderCleaner


def main():
	app = Application()
	return app.run(sys.argv)

class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.github.Latesil.folder-cleaner",
                        flags=Gio.ApplicationFlags.FLAGS_NONE, **kwargs)

        self.window = None

        GLib.set_application_name('Folder Cleaner')
        GLib.set_prgname("com.github.Latesil.folder-cleaner")

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        if not self.window:
            self.window = FolderCleaner(self)

        self.window.present()

    def on_quit(self, action, param):
        self.quit()

if __name__ == "__main__":
    main()