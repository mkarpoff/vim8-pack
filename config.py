#! /usr/bin/env python3

from pathlib import Path
import json

config_file = Path( Path.home(), '.vim-pack', 'vim-pack.conf' )

default_configs = {
    'configs' : {
        'install_dir' : str(Path.home()) + '/.vim/pack/_vim-pack-git-plugins/',
        'threads'     : 8
    },
    'packages'    : {}
}


class Config:

    __configs__ = { }
 

    def add_package(self, name, url, start_opt, install_dir):
        self['packages'][name] = {
                'name'          : name,
                'url'           : url,
                'start_opt'     : start_opt,
                'install_dir'   : install_dir
            }
    def get_packages(self):
        return self.__configs__['packages']

    def create_default_config_file(self):
        if not config_file.parent.is_dir():
            config_file.parent.mkdir()
        with config_file.open('w') as fp:
            json.dump(default_configs, fp, indent=4)

    def merge_missing_configs(self):
        default_configs.update(self.__configs__)
        with config_file.open('w') as fp:
            json.dump(default_configs, fp, indent=4)


    def load_config_file(self):
        with config_file.open('r') as fp:
            self.__configs__ = json.load(fp)

    def load_configs(self):
        if not config_file.is_file():
            self.create_default_config_file()
        self.load_config_file()
        self.merge_missing_configs()

    ### Accessors for the internal configurations
    def __getitem__(self, key):
        return self.__configs__['configs'].__getitem__(key)

    def __setitem__(self, key, value):
        return self.__configs__['configs'].__setitem__(key, value)

    def __delitem__(self, key):
        return self.__configs__['configs'].__delitem__(key)

    def __missing__(self, key):
        return self.__configs__['configs'].__missing__(key)

    def __iter__(self):
        return self.__configs__['configs'].__iter__()

    def __reversed__(self):
        return self.__configs__['configs'].__reversed__()

    def __contains__(self, key):
        return self.__configs__['configs'].__contains__(key)

    def __len__(self):
        return self.__configs__['configs'].__len__()

    def __length_hint__(self):
        return self.__configs__['configs'].__length_hint__()

    def __str__(self):
        return self.__configs__['configs'].__str__()
