
def color(this_color, string):
    return "\033[" + str(this_color) + "m" + string + "\033[0m"

def message(mess, col="MESSAGE"):
	if col == "OK":
		print('%s' % color("1;32", "[+] " + mess ))
	elif col == "WARNING":
		print('%s' % color("1;33", "[!] " + mess ))
	elif col == "ERROR":
		print('%s' % color("1;31", "[-] " + mess ))
	elif col == "MESSAGE":
		print('%s' % color("1;37", "[*] " + mess ))
		
'''		
message("ok", "OK")
message("ok", "WARNING")
message("ok", "ERROR")
message("ok", "MESSAGE")
'''
