
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
# This file is part of Slixmpp.
# See the file LICENSE for copying permission.
from slixmpp.plugins.base import register_plugin

from slixmpp.plugins.xep_0107 import stanza
from slixmpp.plugins.xep_0107.stanza import UserMood
from slixmpp.plugins.xep_0107.user_mood import XEP_0107


register_plugin(XEP_0107)
