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
        /* Translators: Replace "translator-credits" with your names, one name per line */
        aboutDialog.translator_credits = _("Stason");
        aboutDialog.program_name = _("Folder Cleaner");
        aboutDialog.copyright = 'Copyright ' + String.fromCharCode(0x00A9) + ' 2019' + String.fromCharCode(0x2013) + 'Late Inc.';
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
    
    _open() {
        log('Open');
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
        this._main_label = builder.get_object('main_label');
        
        this._model_button_about.connect('clicked', () => { this._showAbout(); });
        this._model_button_add.connect('clicked', () => { this._add(); });
        this._main_button_sort.connect('clicked', () => { this._sort(); });
        this._main_button_open.connect('clicked', () => { this._open(); });
    }
};

let app = new FolderCleaner();
app.application.run(ARGV);
