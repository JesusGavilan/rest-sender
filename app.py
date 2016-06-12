__author__ = 'jesus.gavilan'
"""
REST-SENDER API REST ROUTES
"""
import falcon
from resources.testbeds import TestbedsCollection

api = application = falcon.API()

api.add_route("/api/v0.1/testbeds", TestbedsCollection())
#api.add_route("/api/v0.1/testbeds/{testbed_id}")
#api.add_route("/api/v0.1/testbed/{testbed_id}/execution")
#api.add_route("/api/v0.1/testbed/{testbed_id}/results")
#api.add_route("/api/v0.1/testbed/{testbed_id}/results/{testbed_id}")
#api.add_route("/api/v0.1/schemas")
#api.add_route("/api/v0.1/schemas/{schema_id}")