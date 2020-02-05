import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, GLib
from helpers import get_files_and_folders

file = Gio.File.new_for_path('/home/late/Documents/testphoto/efwerwefw')
destination_for_photo = Gio.File.new_for_path('/home/late/Documents/testphoto/20191226')
Gio.File.make_directory_with_parents(file)

# file.move(destination_for_photo, Gio.FileCopyFlags.NONE)


# for f in files:
#     if GLib.file_test(f, GLib.FileTest.EXISTS | GLib.FileTest.IS_REGULAR):
#         print(f, 'file')

# print("------")

# for f in folders:
#     if GLib.file_test(f, GLib.FileTest.EXISTS | GLib.FileTest.IS_DIR):
#         print(f, 'folder')


# path = '/home/late/Documents/testphoto/IMG_20200131_153933.jpg'
# output = '/home/late/Documents/testphoto/tost.jpg'

# myfile = Gio.File.new_for_path(path)
# output_folder = Gio.File.new_for_path(output)
# folder = Gio.File.new_for_path('/home/late/Documents/testphoto/')

# # myfile.copy_async(output_folder, Gio.FileCopyFlags.NONE, GLib.PRIORITY_DEFAULT)


# enumerator = folder.enumerate_children("standard::*", 
#                                         Gio.FileQueryInfoFlags.NONE)

# info = enumerator.next_file()
# while info is not None:
#     if info.get_file_type() == Gio.FileType.DIRECTORY:
#         print(folder.get_path() + info.get_name())
#         info = enumerator.next_file()
#     else:
#         print(info.get_content_type())
#         info = enumerator.next_file()