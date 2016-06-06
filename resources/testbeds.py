__author__ = 'jesus.gavilan'
import logging
import falcon

"""
Testbeds Collection resource
"""
class TestbedsCollection(object):
    """
    TO-DO
    """
    def __init__(self):
        """
        TO-DO
        :return:
        """

        self.logger = logging.getLogger(__name__)

    def on_get(self, req, resp):
        """
        GET testbed collection resource
        TO-DO
        """

"""
Testbeds Item resource
"""
class TestbedsItem(object):
    """
    TO-DO
    """
    def __init__(self):
        """
        :return:
        """
        self.logger = logging.getLogger(__name__)
        #TO-DO

    def on_get(self,req, resp, testbed_id):
        """
        GET testbed item resource
        :param req:
        :param resp:
        :param testbed_id:
        :return:
        """
        #TO-DO

    def on_post(self, req, resp):
        """
        POST testbed item resource
        :param req:
        :param resp:
        :return:
        """
        #TO-DO

    def on_put(self, req, resp):
        """
        PUT testbed item resource
        :param req:
        :param resp:
        :return:
        """
        #TO-DO
    def on_delete(self, req, resp, testbed_id):
        """
        DELETE testbed item resource
        :param req:
        :param resp:
        :param testbed_id:
        :return:
        """
        #TO-DO




