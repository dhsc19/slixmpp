
# slixmpp.xmlstream.handler.collector
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Part of Slixmpp: The Slick XMPP Library
# :copyright: (c) 2012 Nathanael C. Fritz, Lance J.T. Stout
# :license: MIT, see LICENSE for more details
import logging
from queue import Queue, Empty

from slixmpp.xmlstream.handler.base import BaseHandler


log = logging.getLogger(__name__)


class Collector(BaseHandler):

    """
    The Collector handler allows for collecting a set of stanzas
    that match a given pattern. Unlike the Waiter handler, a
    Collector does not block execution, and will continue to
    accumulate matching stanzas until told to stop.

    :param string name: The name of the handler.
    :param matcher: A :class:`~slixmpp.xmlstream.matcher.base.MatcherBase`
                    derived object for matching stanza objects.
    :param stream: The :class:`~slixmpp.xmlstream.xmlstream.XMLStream`
                   instance this handler should monitor.
    """

    def __init__(self, name, matcher, stream=None):
        BaseHandler.__init__(self, name, matcher, stream=stream)
        self._payload = Queue()

    def prerun(self, payload):
        """Store the matched stanza when received during processing.

        :param payload: The matched
            :class:`~slixmpp.xmlstream.stanzabase.ElementBase` object.
        """
        self._payload.put(payload)

    def run(self, payload):
        """Do not process this handler during the main event loop."""
        pass

    def stop(self):
        """
        Stop collection of matching stanzas, and return the ones that
        have been stored so far.
        """
        self._destroy = True
        results = []
        try:
            while True:
                results.append(self._payload.get(False))
        except Empty:
            pass

        self.stream().remove_handler(self.name)
        return results
