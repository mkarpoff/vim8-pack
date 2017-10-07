#! /usr/bin/env python3

from pathlib import Path
import json
import sys
if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    raise "Must be greater than or equal to Python 3.5 to run this script"
name="name"
target="target"

with open("files.json") as data_files:
    files = json.load(data_files)


def link(filename, target):
    target_path = Path(target).expanduser()
    source_path = Path(filename).expanduser()
    if (not source_path.exists()):
        print("[%-30s] -> [%-40s] Not linked. Source missing" %(source_path, target_path))
        return
    if (target_path.exists()):
        print("[%-30s] -> [%-40s] Not linked. Target exists" %(source_path, target_path))
        return
    if (target_path.is_symlink()):
        print("[%-30s] -> [%-40s] Target exist and is symlink" %(source_path, target_path))
        if (query_yes_no("Remove and remake? ")):
            target_path.unlink()
            print("[%-30s] -> [%-40s] Target old link removed" %(source_path, target_path))
        else:
            return
    if (not target_path.parent.exists()):
        print("[%-30s] -> [%-40s] Creating missing parent directory" %(source_path, target_path))
        target_path.parent.mkdir(parents=True);
    target_path.symlink_to(source_path.resolve())
    print("[%-30s] -> [%-40s] Symlink created successfully" %(source_path, target_path))


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
