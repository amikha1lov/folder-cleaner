import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from helpers import get_files_and_folders, operations, folders_made

folders, files = get_files_and_folders('/home/late/test')

for f in files:
    content_type, val = Gio.content_type_guess(f)
    print(content_type)