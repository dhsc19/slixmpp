
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
# This file is part of Slixmpp.
# See the file LICENSE for copying permission.

from slixmpp.stanza import Message
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.plugins.xep_0071 import stanza, XHTML_IM


class XEP_0071(BasePlugin):

    name = 'xep_0071'
    description = 'XEP-0071: XHTML-IM'
    dependencies = {'xep_0030'}
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Message, XHTML_IM)

    def session_bind(self, jid):
        self.xmpp['xep_0030'].add_feature(feature=XHTML_IM.namespace)

    def plugin_end(self):
        self.xmpp['xep_0030'].del_feature(feature=XHTML_IM.namespace)
