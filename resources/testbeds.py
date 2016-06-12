__author__ = 'jesus.gavilan'
import logging
import falcon
from bson import Binary, Code
from bson.json_util import dumps,loads
from mapper.testbeddb import TestbedMapper
from utils.jsonmsg import *
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
        :param req:HTTP request of testbed collection resource
        :param resp: HTTP response of the testbed collection resource
        """
        try:
            # Get all testbed collection data and parsed to JSON
            tbList = TestbedMapper().getAll()
            success_msg = success
            success_msg["data"] = tbList
            # Send 200 OK response with the tesbed collection data
            resp.status = falcon.HTTP_200
            resp.body = dumps(success_msg)
        except Exception as ex:
            self.logger.error("Error getting testbed collection. Info: ", ex)
            raise falcon.HTTPError(falcon.HTTP_500, description="DB Error")

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




