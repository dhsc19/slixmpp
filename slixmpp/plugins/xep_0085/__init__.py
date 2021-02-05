
# Slixmpp: The Slick XMPP Library
# Copyright (C) 2011 Nathanael C. Fritz, Lance J.T. Stout
# This file is part of Slixmpp.
# See the file LICENSE for copying permissio
from slixmpp.plugins.base import register_plugin

from slixmpp.plugins.xep_0085.stanza import ChatState
from slixmpp.plugins.xep_0085.chat_states import XEP_0085


register_plugin(XEP_0085)
