import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/preferences.ui')
class PreferencesWindow(Gtk.Dialog):

    __gtype_name__ = "_preferences_dialog"

    def __init__(self, app, *args, **kwargs):
        super().__init__(**kwargs)