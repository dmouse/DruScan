#!/usr/bin/env python

import signal
import sys

from color import message
from core  import signal_handler
from core  import update
from core  import search
from core  import detect_version
from ops 	 import opsx


try:
	
	signal.signal(signal.SIGINT, signal_handler)
	o = opsx()

	if o.update_modules:
		update("modules", o.limit)
		message("Update modules. Done.","OK")
		exit
	elif o.update_themes:
		update("themes", o.limit)
		message("Update themes. Done.","OK")
		exit
	
	
	
	if o.url != None:
		
		site_version = detect_version(o.url)
		message("Posible version " + str(site_version), "WARNING")
		
		if o.modules:
			search ("http://" + o.url, "modules" , version = site_version )
		elif o.themes:
			search ("http://" + o.url, "themes"  , version = site_version )
			
except ImportError:
	print " "
