import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init('com.github.Latesil.folder-cleaner')

notification = Notify.Notification.new('Title', "body")

notification.show()