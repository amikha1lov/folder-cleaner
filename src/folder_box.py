import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/folder-box.ui')
class FolderBox(Gtk.EventBox):

    __gtype_name__ = "_folder_box"

    _folder_box_label = Gtk.Template.Child()

    def __init__(self, app, *args, **kwargs):
        super().__init__(**kwargs)

        #self._folder_box_label.set_label("Folder Label")


    @Gtk.Template.Callback()
    def on__sort_button_clicked(self, button):
        print('on__sort_button_clicked')


    @Gtk.Template.Callback()
    def on__sort_files_clicked(self, button):
        print('on__sort_files_clicked')


    @Gtk.Template.Callback()
    def on__open_folder_clicked(self, button):
        print('on__open_folder_clicked')


    @Gtk.Template.Callback()
    def on__close_folder_clicked(self, button):
        print('on__close_folder_clicked')