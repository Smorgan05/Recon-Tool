from subprocess import check_output

out = check_output(["whatweb", "-a 3", "www.wired.com"])
result = String_Clean(out)

def String_Clean(multi_string):
	import re
	ansi_regex = r'\x1b(' \
				 r'(\[\??\d+[hl])|' \
				 r'([=<>a-kzNM78])|' \
				 r'([\(\)][a-b0-2])|' \
				 r'(\[\d{0,2}[ma-dgkjqi])|' \
				 r'(\[\d+;\d+[hfy]?)|' \
				 r'(\[;?[hf])|' \
				 r'(#[3-68])|' \
				 r'([01356]n)|' \
				 r'(O[mlnp-z]?)|' \
				 r'(/Z)|' \
				 r'(\d+)|' \
				 r'(\[\?\d;\d0c)|' \
				 r'(\d;\dR))'
	ansi_escape = re.compile(ansi_regex, flags=re.IGNORECASE)
	converted = multi_string.decode("utf-8")
	Clean = ansi_escape.sub('', converted)
	return Clean
