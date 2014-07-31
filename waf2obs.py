#!/usr/bin/env python

import os 
import os.path



def getDependencies(path):

    dep_arr = []

    # --{0}-path=bundle_dependencies/{1}/".format('-'.join(lib.split('-')[:-1]), lib)
    
    for f in os.listdir(path):
        if os.path.isdir(path + "/" + f):
            print(f)
            getNoneMasterDependency(path, f,dep_arr)
            
    return dep_arr

def getNoneMasterDependency(base, path, dep_arr):
    for f in os.listdir(base + "/" + path):
        if not "master" in f:
            print(f)
            
            dep_arr.append("--{0}-path=bundle_dependencies/{1}/".format('-'.join(path.split('-')[:-1]), path)  + f)
#            dep_arr.append(path + "/" + f + "/")


def createWafBashScript(dep_arr):
    file = open("build.sh", "w")
    file.write("#!/usr/bin/env bash\n")
    file.write("\n\n\n")
    
    waf_conf_str = "python waf configure --bundle=NONE " + createMonsterPath(dep_arr)
    
    file.write(waf_conf_str + "\n")
    file.write("python waf build")

    file.close()

def createMonsterPath(dep_arr):
    monster_path = ""
    for s in dep_arr:
        monster_path = monster_path + s + " "
        
    monster_path = monster_path[: -1]
    return monster_path



PATH = "bundle_dependencies"
deps =  getDependencies(PATH)
createWafBashScript(deps)

