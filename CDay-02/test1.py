# coding:utf8
# Author :       huxiaoyi
# Date：         2019-04-15
from cmd import Cmd
import os
import sys


class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, arg):
        print("hello", arg)


if __name__ == '__main__':
    cli = Cli()
    cli.cmdloop()
