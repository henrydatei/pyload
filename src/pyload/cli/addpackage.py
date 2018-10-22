# -*- coding: utf-8 -*-
# @author: RaNaN
from builtins import _

from pyload.cli.handler import Handler
from pyload.cli.printer import *


class AddPackage(Handler):
    """
    let the user add packages.
    """

    def init(self):
        self.name = ""
        self.urls = []

    def onEnter(self, inp):
        if inp == "0":
            self.cli.reset()

        if not self.name:
            self.name = inp
            self.setInput()
        elif inp == "END":
            # add package
            self.client.addPackage(self.name, self.urls, 1)
            self.cli.reset()
        else:
            if inp.strip():
                self.urls.append(inp)
            self.setInput()

    def renderBody(self, line):
        println(line, white(self._("Add Package:")))
        println(line + 1, "")
        line += 2

        if not self.name:
            println(line, self._("Enter a name for the new package"))
            println(line + 1, "")
            line += 2
        else:
            println(line, self._("Package: {}").format(self.name))
            println(line + 1, self._("Parse the links you want to add."))
            println(line + 2, self._("Type {} when done.").format(mag("END")))
            println(line + 3, self._("Links added: ") + mag(len(self.urls)))
            line += 4

        println(line, "")
        println(line + 1, mag("0.") + self._(" back to main menu"))

        return line + 2
