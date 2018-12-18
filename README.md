# vim8-pack
Some simple tools to maintain and update git based packages for vim 8. Currently it is for managing packages designed
for vim 7 and earlier. This is because I have yet to find a package that properly conforms to the vim8 package standard.
I intend tools for handling vim8 compatible packages as well. Development is ongoing so while it functions, there are
bugs and changes that are ongoing. Feel free to open issues. I'll get to them as I can.

## How to install
### Recomended Way
Requires python3.4
```bash
git clone https://github.com/mkarpoff/vim8-pack.git ~/.local/src/vim8-pack
cd ~/.local/src/vim8-pack
./linkall.py
```
Make sure ~/.local/bin is added to you path
### Recomended Way \# 2
clone the files into whatever directory you'd like

```bash
cd <some directory in you path>
ln -s <PATH>/<TO>/<Repo>/vim-pack vim-pack
ln -s <PATH>/<TO>/<Repo>/vim-pack-get vim-pack-get
ln -s <PATH>/<TO>/<Repo>/vim-pack-update vim-pack-update
ln -s <PATH>/<TO>/<Repo>/vim-pack-upgrade vim-pack-upgrade
ln -s <PATH>/<TO>/<Repo>/vim-pack-remove vim-pack-remove
ln -s <PATH>/<TO>/<Repo>/vim-pack-import vim-pack-inport
ln -s <PATH>/<TO>/<Repo>/vim-pack-export vim-pack-export
```

I suggest using symbolic links so that if you'd like to keep up to date with changes then all you would have to do is cd
to where you cloned the repo and type.

```bash
git pull
```

This avoids having to move the files after setup

### Alternative way
Clone wherever and place the files somewhere in your path

## How to use

### To upgrade package

```bash
vim-pack upgrade [-s|--silent] [-d <dir>| --git-dir=<dir>]
```
`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`
`-h | --help` display a really helpful message about how to use the program
`-s | --silent` to hide output that normally goes to stdout
`-t | --threads` Cause the script to pull multiple concurently. Will run with <num threads> threads. The default value
is value is 1 thread per virtual core provided by the command nproc. 
Note: Only works if moreutils parallel or GNU parallel is installed otherwise it will do nothing 
`-v | --verbose` Prints out verbose output.


### To get list of upgrades for package

```bash
vim-pack update [-s|--silent] [-d <dir>| --git-dir=<dir>]
```
`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`


### To download a new package

```bash
vim-pack get [-s|--silent] [-d <dir>| --git-dir=<dir>] <opt|start> <URL> [<new name>]
vim-pack install [-s|--silent] [-d <dir>| --git-dir=<dir>] <opt|start> <URL> [<new name>]
```
`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`

use `opt` or `start` to specify whether it should be a optional package or
loaded for every time if you use `opt` you will need to specifically add the
package using the vim 8 command `packadd <package name>`

`<URL>` specifies the directory the package should be pulled from. Internally
this is a git clone command

`[<new name>]` can be used if you would like to load the package under a
different name

### To remove a new package

```bash
vim-pack remove [-s|--silent] [-d <dir>| --git-dir=<dir>] [<opt|start>] <name>
```

`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`

Use `opt` or `start` to specify whether the package is an optional package or
loaded for every time. If neither are supplied then it will attempt to remove from both.

`[<name>]` specifies the package name

### To export package lists

```bash
vim-pack export [-s|--silent] [-d <dir>| --git-dir=<dir>] [<file>]
vim-pack list   [-s|--silent] [-d <dir>| --git-dir=<dir>] <file>
```

`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`

If `<file>` is provided then the list of packages will be exported to a file following the INI file format. If the `-s`
or `--silent` option arguments are given then an output file is mandatory. This is useful for transferring
configurations across machines and for listing all installed packages

### To import package lists

```bash
vim-pack import [-s|--silent] [-d <dir>| --git-dir=<dir>] <file>
```

`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package directory by default it is
`$HOME/.vim/pack/git-plugins`

`<file>` is the name of the required INI format file. This can be generated using `vim-pack export` this is useful for
transferring configurations between machines.

## Completion
To make this easier to use bash completion functionality has been added. This program is designed to be easily used
without `sudo` so by default it uses the user level completion configuration and not the system wide completion
configuration. This means that it will place the completion script in `~/.bash-completion.d/` and if there is no
`~/.bash_compltion` it will add a link for one.
