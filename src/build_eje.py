import sys
path = sys.argv[1]
filefornew = path[:-6] + ".cmd"
sysop = open(filefornew, "w")
sysop.write(f"marfhing {path}")
