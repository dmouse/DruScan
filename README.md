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

Update Modules
==============
$ ./druscan.py --update-modules --limit 10 # default 3

Update Themes
==============
$ ./druscan.py --update-themes --limit 2 # default 3

Search Modules
==============
$ ./druscan.py --url drupal-site.com --modules

Search Themes
==============
$ ./druscan.py --url drupal-site.com --themes


