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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from constants import folder_cleaner_constants as constants

@Gtk.Template.from_file('/home/late/Programs/folder-cleaner/src/preferences.ui')
class PreferencesWindow(Gtk.Dialog):

    __gtype_name__ = "_preferences_dialog"

    def __init__(self, app, *args, **kwargs):
        super().__init__(**kwargs)