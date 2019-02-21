#!/usr/bin/python

'''

   _____                      _  _____ _               _
  / ____|                    (_)/ ____| |             | |
 | (___   ___  ___ _   _ _ __ _| |    | |__   ___  ___| | __
  \___ \ / _ \/ __| | | | '__| | |    | '_ \ / _ \/ __| |/ /
  ____) |  __/ (__| |_| | |  | | |____| | | |  __/ (__|   <
 |_____/ \___|\___|\__,_|_|  |_|\_____|_| |_|\___|\___|_|\_\


            Written by Yessine Taktak
                        (https://github.com/yassintaktak)
            For more please visit https://seuriflow.com/

            use at your own risk !

'''

import sys, os
import importlib
import thread
import time

try:
    # Fix UTF8 output issues on Windows console.
    # Does nothing if package is not installed
    from win_unicode_console import enable
    enable()
except ImportError:
    pass

sys.path.append('./modules')

module_used = ''
saving_file = 'output.txt'
threading = False
loaded_module = ''
combo_list = []
debug = True
working_items = 0
not_working_items = 0

def checkmodule(module):
    try:
        global module_class
        if(os.path.isfile("./modules/"+str(module)+"_module.py")):
            m = importlib.import_module(str(module)+"_module")
            module_class = m
            return True
        else:
            return False
    except:
        pass

def set_module(module):
    if(checkmodule(module)):
        module_used = module
        loaded_module = module
        return True
    else:
        return False

def checkThread(thread, item):
    try:
        combo_items = combo_item.split(':')
        checking_module = loaded_module.check(combo_items)
        if(checking_module):
            working_items += 1
            if(debug):
                if(loaded_module.checkReturnOptionsSTR()):
                    print(str(combo_items)+" : Working | "+str(checking_module))
                else:
                    print(str(combo_items)+" : Working.")
            with open(saving_file, 'a+') as f:
                if(loaded_module.checkReturnOptionsSTR()):
                    f.write(str(combo_items)+' | '+str(checking_module)+'\n')
                else:
                    f.write(str(combo_items)+'\n')
        else:
            not_working_items += 1
            if(debug):
                print(str(combo_items)+" : Not working.")
    except:
        print("Error processing : "+str(combo_item))
        pass

if __name__ == '__main__':
    if(len(sys.argv) < 3):
        print("Unspecified necessary arguments, exiting.")
    else:
        if(set_module(sys.argv[1])):
            print("Module used : "+str(sys.argv[1]))
            loaded_module = module_class.Main()
        else:
            print("The module specified is not found, exiting.")
            sys.exit(0)
        if(os.path.isfile(sys.argv[2])):
            print("Combo loaded : "+str(sys.argv[2]))
            combo_list = open(sys.argv[2]).readlines()
        else:
            print("Combo file not found, exiting.")
            sys.exit(0)
    if(len(sys.argv) >= 4):
        saving_file = sys.argv[3]
        print("Saving file : "+str(saving_file))
    if(len(sys.argv) >= 5):
        if(sys.argv[4] == "1"):
            threading = True
            print("Using threading.")
    if(len(sys.argv) == 6):
        if(sys.argv[5] == "0"):
            debug = False

    if(loaded_module != ''):
        # Handling everything here!
        if(loaded_module.checkLoadingState()):
            for combo_item in combo_list:
                combo_item = combo_item.rstrip()
                if(threading == False):
                    try:
                        combo_items = combo_item.split(':')
                        checking_module = loaded_module.check(combo_items)
                        if(checking_module):
                            working_items += 1
                            if(debug):
                                if(loaded_module.checkReturnOptionsSTR()):
                                    print(str(combo_items)+" : Working | "+str(checking_module))
                                else:
                                    print(str(combo_items)+" : Working.")
                            with open(saving_file, 'a+') as f:
                                if(loaded_module.checkReturnOptionsSTR()):
                                    f.write(str(combo_items)+' | '+str(checking_module)+'\n')
                                else:
                                    f.write(str(combo_items)+'\n')
                        else:
                            not_working_items += 1
                            if(debug):
                                print(str(combo_items)+" : Not working.")
                    except:
                        print("Error processing : "+str(combo_item))
                        pass
                else:
                    print("Threading not available yet")

            print("+----------------------------------------+")
            print("Job done.")
            print("Total working : "+str(working_items))
            print("Total failed : "+str(not_working_items))
            print("+----------------------------------------+")
