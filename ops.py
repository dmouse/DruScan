import argparse

def opsx():
	parser = argparse.ArgumentParser(conflict_handler='resolve', description='Drupal scanner by @dmouse')

	#
	# Core options: update modules, update themes and limit pages on drupal.org
	#

	core = parser.add_argument_group('Core')
	core.add_argument('--update-modules', action="store_true", dest="update_modules", help='Update list modules'     , default=False )
	core.add_argument('--update-themes' , action="store_true", dest="update_themes" , help='Update list themes'      , default=False  )
	core.add_argument('--limit'         , action="store", dest="limit"         , help='Limit page on drupal.org', type=int , default=3)


	#
	# Testing Options: site url, modules and themes path, search users, modules and themes
	#

	test = parser.add_argument_group('Testing')
	test.add_argument("--url"         , action="store"     , dest="url"    , help="URL Drupal Site http://drupalsite.com", type=str )

	test.add_argument("--modules"     , action="store_true", dest="modules", help="Search modules"                       , default=False)
	test.add_argument("--themes"      , action="store_true", dest="themes" , help="Search themes"                        , default=False)
	test.add_argument("--users"       , action="store_true", dest="users"  , help="Search users"                         , default=False)
	test.add_argument("--paths"       , action="store_true", dest="paths"  , help="Search paths"                         , default=False)

	parser.add_argument('--version', action='version', version='%(prog)s 0.7 alpha')

	return parser.parse_args()
