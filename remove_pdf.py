import os,sys

print(os.path.basename(os.path.abspath(sys.argv[0])).replace(".py",""))