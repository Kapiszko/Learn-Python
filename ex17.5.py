from sys import argv; script, from_file, to_file = argv; in_file = open(from_file).read(); out_file = open(to_file, 'w'); out_file.write(in_file); out_file.close()
