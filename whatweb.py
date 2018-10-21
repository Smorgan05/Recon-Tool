from subprocess import check_output
out = check_output(["whatweb", "-a 3", "www.wired.com"])
result = String_Clean(out)

def String_Clean(multi_string):
	import re
	ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
	clean = ansi_escape.sub('', out.decode('unicode_escape'))
	return clean
