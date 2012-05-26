
def color(this_color, string):
    return "\033[" + str(this_color) + "m" + string + "\033[0m"

def message(mess, search = "-", col="MESSAGE"):
	if col == "OK":
		print('%s' % color("1;32", "[ " + search + " ] " + mess ))
	elif col == "WARNING":
		print('%s' % color("1;33", "[ " + search + " ] " + mess ))
	elif col == "ERROR":
		print('%s' % color("1;31", "[ " + search + " ] " + mess ))
	elif col == "MESSAGE":
		print('%s' % color("1;37", "[ " + search + " ] " + mess ))
		
'''		
message("ok", "OK")
message("ok", "WARNING")
message("ok", "ERROR")
message("ok", "MESSAGE")
'''
