#!/usr/bin/env python

import signal
import sys
import core

from color import message
from core  import signal_handler
from core  import update
from core  import search
from core  import detect_version
from core	 import search_users
from core  import search_urls
from ops 	 import opsx


try:
	
	signal.signal(signal.SIGINT, signal_handler)
	o = opsx()

	if o.update_modules:
		update("modules", o.limit)
		message("Update modules. Done.",core.M_UPDATE, "OK")
		exit
	elif o.update_themes:
		update("themes", o.limit)
		message("Update themes. Done." ,core.M_UPDATE,"OK")
		exit
	
	
	
	if o.url != None:
		
		site_version = detect_version(o.url)
		message("Posible version " + str(site_version),core.M_VERSION, "WARNING")
		message("\t" + o.url + "/CHANGELOG.txt",core.M_FILE, "WARNING")
		
		if o.modules:
			search ( o.url, "modules" , version = site_version )
			
		if o.themes:
			search ( o.url, "themes"  , version = site_version )
		
		if o.users:
			if o.limit != 3:
				ulimit = o.limit
			else:
				ulimit = 20
		
			search_users(o.url, ulimit)
		
		if o.paths:
			search_urls(o.url)
			
except ImportError:
	print " "
