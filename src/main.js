imports.searchPath.unshift("/home/late/Documents/folder-cleaner/src");

pkg.initGettext();
pkg.initFormat();
pkg.require({ 'Gdk': '3.0',
              'GLib': '2.0',
              'GObject': '2.0',
              'Gtk': '3.0' });
              
const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const GObject = imports.gi.GObject;
const Gtk = imports.gi.Gtk;
const Gdk = imports.gi.Gdk;
const System = imports.system
let path;
let configFile = GLib.get_home_dir() + '/.folder-cleaner.conf';

if (GLib.file_test(configFile, GLib.FileTest.EXISTS)) {
    path = imports.byteArray.toString(GLib.file_get_contents(configFile)[1]);
} else {
    Gio.file_new_for_path(configFile);
    GLib.file_set_contents(configFile, "file://" + GLib.get_home_dir() + "/Downloads");
    path = imports.byteArray.toString(GLib.file_get_contents(configFile)[1]);
}

class FolderCleaner {
    constructor() {
        this.application = new Gtk.Application();
        this.application.connect('activate', this._onActivate.bind(this));
        this.application.connect('startup', this._onStartup.bind(this));
    }

    _onActivate() {
        this._window.show_all();
    }
    
    _showAbout() {
        let aboutDialog = new Gtk.AboutDialog();
        aboutDialog.artists = [ 'Late' ];
        aboutDialog.authors = [ 'Lateseal' ];
        aboutDialog.translator_credits = "Stason";
        aboutDialog.program_name = _("Folder Cleaner");
        aboutDialog.copyright = _('Copyright ') + String.fromCharCode(0x00A9) + ' 2019' + String.fromCharCode(0x2013) + 'Late Inc.';
        aboutDialog.license_type = Gtk.License.GPL_3_0;
        aboutDialog.logo_icon_name = pkg.name;
        aboutDialog.version = pkg.version;
        aboutDialog.website = 'placeholder';
        aboutDialog.wrap_license = true;
        aboutDialog.modal = true;
        aboutDialog.transient_for = this._window;

        aboutDialog.show();
        aboutDialog.connect('response', function() {
            aboutDialog.destroy();
        });
    }
    
    _add() {
        log('Add');
    }
    
    _sort() {
        log('Sort');
    }
    
    _folder() {
        path = this._main_button_folder.get_uri();
        this._main_button_folder.set_current_folder_uri(path);
        GLib.file_set_contents(configFile, path);
    }
    
    _open() {
        GLib.spawn_command_line_async("xdg-open " + this._main_button_folder.get_current_folder());
    }

    _onStartup() {
        let builder = new Gtk.Builder();
        builder.add_from_file('/home/late/Documents/folder-cleaner/ui/main.ui');
        this._window = builder.get_object('main_window');
        this.application.add_window(this._window);
        
        this._model_button_about = builder.get_object('model_button_about');
        this._model_button_add = builder.get_object('model_button_add');
        this._main_button_sort = builder.get_object('main_button_sort');
        this._main_button_open = builder.get_object('main_button_open');
        
        this._main_button_folder = builder.get_object('main_button_folder');
        this._main_button_folder.set_current_folder_uri(path);
        
        this._model_button_about.connect('clicked', () => { this._showAbout(); });
        this._model_button_add.connect('clicked', () => { this._add(); });
        this._main_button_sort.connect('clicked', () => { this._sort(); });
        this._main_button_open.connect('clicked', () => { this._open(); });
        this._main_button_folder.connect('file-set', () => { this._folder(); });
    }
};

let app = new FolderCleaner();
app.application.run(ARGV);
