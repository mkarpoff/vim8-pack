#! /usr/bin/env python3

import argparse
from config import Config

def generate_parser(configs):
    # The parent_parser parser for all common arguments
    parent_parser = argparse.ArgumentParser(add_help = False)
    verb_silent_group = parent_parser.add_mutually_exclusive_group()
    verb_silent_group.add_argument( '-v', '--verbose', action = 'store_true', help = 'Enables verbose output' )
    verb_silent_group.add_argument( '-s', '--silent', action = 'store_true', help = 'Silences all output' )
    parent_parser.add_argument( '-d', '--pack-dir',
            default = configs['install_dir'],
            help = 'The directory for storing the pluggins. Default:'+configs['install_dir'])

    # The parent_parser for multithreaded arguments
    mulithreaded_parent_parser = argparse.ArgumentParser(add_help = False)
    mulithreaded_parent_parser.add_argument( '-j', '--jobs', type = int, help = 'Specify the number of cores to use' )

    # Base parser
    parser = argparse.ArgumentParser(
            description = 'A command line base vim8 plugin management system',
            parents=[parent_parser])

    # Command Specific Parsers
    subparsers = parser.add_subparsers(metavar = '<command>',
            dest = 'command',
            help = 'The command must be one of the following:' )

    # install parser
    install_parser = subparsers.add_parser( 'install',
            aliases = [ 'get' ],
            description = 'This command is used to install plugins from git sources.',
            help = 'Used to download a plugin from a git based source',
            parents = [ parent_parser ] )
    install_parser.add_argument( 'start_opt',
            choices = [ 'start','opt' ],
            help = 'use {opt} or {start} to specify whether it should be a optional plugin or loaded for every '
            'time if you use {opt} you will need to specifically add the plugin using the vim 8 command '
            '"packadd {plugin name}"' )
    install_parser.add_argument( 'url',
            help = '<URL> specifies the directory the plugin should be pulled from. Internally this is a git'
            'clone command' )
    install_parser.add_argument( '-n',
            '--name',
            help = 'Can be used if you would like to load the plugin under a different name' )

    # uninstall parser
    uninstall_parser = subparsers.add_parser( 'uninstall',
            aliases = [ 'remove' ],
            description = 'This command removes installed plugins',
            help = 'Used to remove a plugin',
            parents = [ parent_parser ] )

    #uninstall_parser.add_argument( 'start_opt',
    #        choices = [ 'both', 'start', 'opt' ],
    #        help = 'because the plugin can exist in both the start director and opt directory under the same name.'
    #        'Specify from which folder to remove' )
    uninstall_parser.add_argument( 'name', help = 'Name of the plugin to be removed' )

    # list parser
    list_parser = subparsers.add_parser( 'list', help = 'List installed plugins', parents = [ parent_parser ] )

    # Update parser
    update_parser = subparsers.add_parser( 'update',
            aliases = [ 'check' ],
            description = 'Check for any updates and downloads them',
            help = 'Used to find all the plugins that have update formerly called "upgrade"',
            parents = [ parent_parser ] )

    # import parser
    import_parser = subparsers.add_parser( 'import',
            description = 'Installs all the plugins in the provided file using the configuration specified. '
            'Useful for transferring configuration between machines',
            help = 'Import a plugin list',
            parents = [ parent_parser ] )
    import_parser.add_argument( 'file',
            help = 'The name of the required JSON format file. This can be generaged using vim-pack export' )


    # export parser
    export_parser = subparsers.add_parser( 'export',
            description = 'Exports a list of all the plugins installed on this system into the specified file '
            'in the JSON format',
            help = 'Export a plugin list ',
            parents = [ parent_parser ] )
    export_parser.add_argument( 'file',
            help = 'The name of the file that will be generated.' )

    # sync parser
    sync_parser = subparsers.add_parser( 'sync',
            description = 'Imports all files in a plugin list file and exports the plugin list to include missing '
            'installed plugins',
            help = 'Imports all files in a plugin list file and exports the plugin list to include missing '
            'installed plugins',
            parents = [ parent_parser ] )
    sync_parser.add_argument( 'file',
            help = 'The name of the required JSON format file. That will be sync against' )

    return parser
