import os

snipPath = "./snips/"

def snip_path(type, name):
    path_list = snipPath.split("/")
    path_list += type.split("/")
    path_list.append(name)

    path = "/".join(path_list)
    return path

def create_new_type(name):
    path = snip_path(name, "")
    os.mkdir(path)

def create_new_snip(type, name, content):
    path = snip_path(type, name)

    open(path, "w").write(content)

def read_snip(type, name):
    path = snip_path(type, name)

    return open(path).read()