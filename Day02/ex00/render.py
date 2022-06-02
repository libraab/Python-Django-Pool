#!/usr/local/bin/python3
import settings
import sys, re, os

def get_arg(value):
	try:
		return getattr(settings, value)
	except:
		return None
        
def fct(av):
	if len(av) == 2:
		x = av[1].split('.')
		if x[1] != "template":
			print("Error: Wrong extention")
			return
		if len(x) != 2 or len(x[0]) == 0:
			print("Error: Composition name file not is name.template")
			return
		if os.path.exists(av[1]) == False:
			print("Error: file " + av[1] + " cant be opened")
			return
		f = open(x[0] + ".html", "w")
		with open(x[0] + ".template", "r") as template:
			for line in template:
				y = re.findall('{.*?}', line)
				for word in y:
					replace = get_arg(word[1:len(word)-1])
					if replace is not None:
						line = line.replace(word, replace)
				f.write(line)
		f.close()
	else:
		print("Error: Wrong number of argument")
if __name__ == '__main__':
	fct(sys.argv)