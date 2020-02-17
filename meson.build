project(
	'folder-cleaner',
	version: '0.1.0',
	meson_version: '>= 0.50.0',
)

appname = 'com.github.Latesil.folder-cleaner'

i18n  = import('i18n')

subdir('data')
subdir('nautilus-script')
subdir('foldercleaner')

meson.add_install_script('build-aux/meson/postinstall.py')