import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GExiv2', '0.10')
from gi.repository import Gtk, Gio, GLib, GExiv2

notify = Gio.Notification.new('Title')

notify.set_body('Body')

notify.send_notification('com.github.Latesil.folder-cleaner')

