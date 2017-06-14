#! /usr/bin/env python3

from pathlib import Path
import sys
name="name"
target="target"

files=[
    {name:"vim-pack",       target:"~/.local/bin/vim-pack"},
    {name:"vim-pack-get",   target:"~/.local/bin/vim-pack-get"},
    {name:"vim-pack-remove",target:"~/.local/bin/vim-pack-remove"},
    {name:"vim-pack-update",target:"~/.local/bin/vim-pack-update"},
    ]

def link(filename, target):
    target_path = Path(target).expanduser()
    source_path = Path(filename).expanduser()
    if (not source_path.exists()):
        print("[%16s] -> [%s] Not linked. Source missing" %(source_path, target_path))
        return
    if (target_path.exists()):
        print("[%16s] -> [%s] Not linked. Target exists" %(source_path, target_path))
        return
    if (target_path.is_symlink()):
        print("[%16s] -> [%s] Target exist and is symlink" %(source_path, target_path))
        if (query_yes_no("Remove and remake? ")):
            target_path.unlink()
            print("[%16s] -> [%s] Target old link removed" %(source_path, target_path))
        else:
            return
    if (not target_path.parent.exists()):
        print("[%16s] -> [%s] Creating missing parent directory" %(source_path, target_path))
        target_path.parent.mkdir(parents=True);
    target_path.symlink_to(source_path.resolve())
    print("[%16s] -> [%s] symlink created successfully" %(source_path, target_path))
    

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    code source: http://code.activestate.com/recipes/577058/
    """
    valid = {"yes":"yes",   "y":"yes",  "ye":"yes",
             "no":"no",     "n":"no"}
    valid_true = {"yes":"yes",   "y":"yes",  "ye":"yes"}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return (default in valid_true.keys())
        elif choice in valid.keys():
            return (choice in valid_true.keys())
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


for targ in files:
    link(targ[name], targ[target])
