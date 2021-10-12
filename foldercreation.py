import os
import sys
import os.path

# set variable first (linux) 
# export RESEARCH_PATH=/FOLDEROFCHOICE/

# check for env variable
# if set continue else tell there is something wrong
# should work on windows and linux
rPath = os.path.expandvars(R"${RESEARCH_PATH}")

if rPath is "${RESEARCH_PATH}":
	print("No Enviroment Variable RESEARCH_PATH is set");
	exit(1);

# folder not existing
if not os.path.exists(rPath):
	print("Folder is invalid" +rPath);
	exit(1);

# check for arguments in command #
if len(sys.argv) > 1:
	print('Folder Name to be created', sys.argv[1])
	# we use the env variable as base directory
	# go back via /../
	# to be in the folder above the folder
	path = rPath + "/../" + sys.argv[1]
	print('We will save the folder to '+path)
	try:
		os.mkdir(path)
	except OSError:
	    print ("Creation of the folder %s failed" % path)
	else:
	    print ("Successfully created the fodler %s " % path)
else:
	print("No Folder Name was given. usage: python script.py FOLDERNAME")