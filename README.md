DruScan
=======
	$ ./druscan.py -h
	usage: druscan.py [-h] [--update-modules] [--update-themes] [--limit LIMIT]
                  [--url URL] [--modules] [--themes] [--users] [--version]

	Drupal scanner by @dmouse

	optional arguments:
  	-h, --help        show this help message and exit
  	--version         show program's version number and exit

	Core:
  	--update-modules  Update list modules
  	--update-themes   Update list themes
  	--limit LIMIT     Limit page on drupal.org

	Testing:
  	--url URL         URL Drupal Site http://drupalsite.com
  	--modules         Search modules
  	--themes          Search themes
  	--users           Search users
	--paths           Search Paths

Update Modules
==============
	$ ./druscan.py --update-modules --limit 10 # default 3

Update Themes
==============
	$ ./druscan.py --update-themes --limit 2 # default 3

Search Modules
==============
	$ ./druscan.py --url http://drupal-site.com --modules

Search Themes
==============
	$ ./druscan.py --url http://drupal-site.com --themes

Sample
=============
	$ ./druscan.py --url http://sample.com --paths --modules --themes --users --limit 50

	[  Version  ] Posible version 7
	[  File     ] 	http://sample.com/CHANGELOG.txt
	[  File     ] http://sample.com/sites/all/modules/views/CHANGELOG.txt
	[  Version  ] 	3.x-7.x-dev
	[  File     ] http://sample.com/sites/all/modules/ctools/CHANGELOG.txt
	[  Version  ] 	7.x-1.x-dev
	[  File     ] http://sample.com/sites/all/themes/omega/CHANGELOG.txt
	[  Version  ] 	7.x-3.0-rc2
	[  User     ] admin
	[  Path     ] http://sample.com/user
	[  Path     ] http://sample.com/node/add



