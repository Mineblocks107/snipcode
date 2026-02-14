import snipmgr
import sys

if sys.argv[1] == "add":
    if sys.argv[2] == "type":
        snipmgr.create_new_type(sys.argv[3])
    elif sys.argv[2] == "snip":
        snipmgr.create_new_snip(sys.argv[3], sys.argv[4], open(sys.argv[5]).read())
    
elif sys.argv[1] == "put":
    content = snipmgr.read_snip(sys.argv[2], sys.argv[3])
    with open(sys.argv[4], "a") as f:
        f.write("\n##########\n SnipCode \n##########\n")
        f.write(content)