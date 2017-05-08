# vim8-pack
Some simple tools to maintain and update git based packages for vim 8

## How to install
clone the files into whatever director you'd like

```bash
cd <some director in you path>
ln -s <PATH>/<TO>/<Repo>/vim-pack vim-pack
ln -s <PATH>/<TO>/<Repo>/vim-pack-get vim-pack-get
ln -s <PATH>/<TO>/<Repo>/vim-pack-update vim-pack-update
ln -s <PATH>/<TO>/<Repo>/vim-pack-remove vim-pack-remove
```
I suggest using symbolic links so that if you'd like to keep up to date with changes then all you would have to do is cd to where you cloned the repo and type.

```bash
git pull
```

This avoids having to move the files after setup

## How to use

### To download a new package  

```bash
vim-pack update [-s|--silent] [-d <dir>| --git-dir=<dir>] 
```
`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package director by default it is
`$HOME/.vim/pack/git-plugins`


### To download a new package  

```bash
vim-pack get [-s|--silent] [-d <dir>| --git-dir=<dir>] <opt|start> <URL> [<new name>]
```
`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package director by default it is
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
vim-pack remove [-s|--silent] [-d <dir>| --git-dir=<dir>] [<opt|start>] [<name>]
```

`-s| --silent` to hide output that normally goes to stdout

`-d <dir> | --git-dir=<dir>` specify the name for the package director by default it is
`$HOME/.vim/pack/git-plugins`

Use `opt` or `start` to specify whether the package is an optional package or 
loaded for every time. If neither are supplied then the both will be removed.

`[<name>]` specifies the package name 
