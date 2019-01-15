#! /usr/bin/env bash
repo_dir=$HOME/.vim/pack/git-plugins
silent=false
supports_long_opts=false
getopt --test > /dev/null
if (( $? == 4 )); then
	supports_long_opts=true
fi


####
# This handles the optional arguments
###

SHORT=hsd:
LONG=help,silent,git-dir:

if [[ $supports_long_opts == true ]]; then
	PARSED=$(getopt --options $SHORT --longoptions $LONG --name "$0" -- "$@")
else
	PARSED=$(getopt --options $SHORT --name "$0" -- "$@")
fi

if (( $? != 0 )); then
	echo 'Failed to parse arguments'
	exit 2
fi

eval set -- "$PARSED"
while true; do
	case "$1" in
		-h|--help)
			usage=true
			break
			;;
		-d|--git-dir)
			repo_dir=$2
			shift 2
			;;
		-s|--silent)
			silent=true
			shift
			;;
		--)
			shift
			break
			;;
		*)
			shift
			;;
	esac
done

if [[ $usage == true ]]; then
	echo 'usage: vim-pack get     [-s|--silent] [-d <dir>| --git-dir=<dir>] <opt|start> <URL> [<new name>]'
	echo 'usage: vim-pack install [-s|--silent] [-d <dir>| --git-dir=<dir>] <opt|start> <URL> [<new name>]'
	echo
	echo 'use <opt> or <start> to specify whether it should be a optional package or'
	echo 'loaded for every time if you use <opt> you will need to specifically add the'
	echo 'package using the vim 8 command "packadd <package name>"'
	echo
	echo '<URL> specifies the directory the package should be pulled from. Internally'
	echo 'this is a git clone command'
	echo
	echo '[<new name>] can be used if you would like to load the package under a'
	echo 'different name'
	echo
	echo 'options:'
	echo '    -s| --silent'
	echo '        to hide output that normally goes to stdout'
	echo
	echo '    -d <dir> | --git-dir=<dir>'
	echo '        specify the name for the package directory by default it is'
	echo '        $home/.vim/pack/git-plugins'
	echo
	echo 'note:'
	echo '       long options are only available with systems that have an enhanced version'
	echo '       of getopt.'
	if [[ $supports_long_opts == true ]]; then
		echo '       this system does support long options'
	else
		echo '       this system does not support long options'
	fi
	exit 0
fi

start_opt=$1
repo_target=$2
dest_name=$3

if [[ -z $dest_name ]]; then
	dest_name="$repo_dir/$start_opt/$(basename "$repo_target")"
fi

echo "$start_opt"
echo "$repo_target"
echo "$dest_name"

if [[ "$silent" == true ]]; then
	git clone "$repo_target" "$dest_name" > /dev/null
else
	git clone "$repo_target" "$dest_name"
fi
if [[ $? != 0 ]]; then
	exit $?
fi

if [[ -d "$dest_name/doc" ]]; then
	vim +"helptags $dest_name/doc/" +qall
fi
exit 0
