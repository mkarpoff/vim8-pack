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
