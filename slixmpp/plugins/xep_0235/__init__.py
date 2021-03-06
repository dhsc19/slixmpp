
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
# This file is part of Slixmpp.
# See the file LICENSE for copying permission.
from slixmpp.plugins.base import register_plugin

from slixmpp.plugins.xep_0235 import stanza
from slixmpp.plugins.xep_0235.stanza import OAuth
from slixmpp.plugins.xep_0235.oauth import XEP_0235


register_plugin(XEP_0235)
