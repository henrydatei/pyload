# -*- coding: utf-8 -*-
import re
from builtins import _

from pyload.plugins.internal.addon import Addon


class JustPremium(Addon):
    __name__ = "JustPremium"
    __type__ = "addon"
    __version__ = "0.27"
    __status__ = "testing"

    __pyload_version__ = "0.5"

    __config__ = [
        ("activated", "bool", "Activated", False),
        ("excluded", "str", "Exclude hosters (comma separated)", ""),
        ("included", "str", "Include hosters (comma separated)", ""),
    ]

    __description__ = """Remove not-premium links from added urls"""
    __license__ = "GPLv3"
    __authors__ = [
        ("mazleu", "mazleica@gmail.com"),
        ("Walter Purcaro", "vuolter@gmail.com"),
        ("immenz", "immenz@gmx.net"),
    ]

    def init(self):
        self.event_map = {"linksAdded": "links_added"}

    def links_added(self, links, pid):
        hosterdict = self.pyload.pluginManager.hosterPlugins
        linkdict = self.pyload.api.checkURLs(links)

        premiumplugins = set(
            account.type
            for account in self.pyload.api.getAccounts(False)
            if account.valid and account.premium
        )
        multihosters = set(
            hoster
            for hoster in self.pyload.pluginManager.hosterPlugins
            if "new_name" in hosterdict[hoster]
            and hosterdict[hoster]["new_name"] in premiumplugins
        )

        excluded = [
            "".join(
                part.capitalize()
                for part in re.split(r"(\.|\d+)", domain)
                if part != "."
            )
            for domain in self.config.get("excluded")
            .replace(" ", "")
            .replace(",", "|")
            .replace(";", "|")
            .split("|")
        ]
        included = [
            "".join(
                part.capitalize()
                for part in re.split(r"(\.|\d+)", domain)
                if part != "."
            )
            for domain in self.config.get("included")
            .replace(" ", "")
            .replace(",", "|")
            .replace(";", "|")
            .split("|")
        ]

        hosterlist = (
            (premiumplugins | multihosters).union(excluded).difference(included)
        )

        #: Found at least one hoster with account or multihoster
        if not any(True for pluginname in linkdict if pluginname in hosterlist):
            return

        for pluginname in set(linkdict.keys()) - hosterlist:
            self.log_info(self._("Remove links of plugin: {}").format(pluginname))
            for link in linkdict[pluginname]:
                self.log_debug("Remove link: {}".format(link))
                links.remove(link)
