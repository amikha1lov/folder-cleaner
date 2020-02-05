import gi
from gi.repository import Gio

def get_files_and_folders(folder):
        folder_list = []
        files_list = []

        path = Gio.File.new_for_path(folder)
        enumerator = path.enumerate_children(Gio.FILE_ATTRIBUTE_STANDARD_NAME, Gio.FileQueryInfoFlags.NONE)
        info = enumerator.next_file()
        while info is not None:
            if info.get_file_type() == Gio.FileType.DIRECTORY:
                abs_path = path.get_path() + '/' + info.get_name()
                folder_list.append(abs_path)
                info = enumerator.next_file()
            else:
                abs_path = path.get_path() + '/' + info.get_name()
                files_list.append(abs_path)
                info = enumerator.next_file()
         
        return folder_list, files_list