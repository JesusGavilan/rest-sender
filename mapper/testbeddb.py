__author__ = 'jesus.gavilan'

from pymongo import MongoClient
from pymongo import errors
try:
    client = MongoClient('localhost:27017')
    db = client['restSender']
except errors.ConnectionFailure as e:
    print("Could not connect to Mongodb: %s", e)


class TestbedMapper(object):
    collection = db.testbed

    def create(self,data):
        """
        :param data:
        :return:
        """
        try:
            self.collection.insert_one(data)
        except errors as e:
            print("Error inserting testbed document: %s", e)

    def getAll(self):
        """
        :return:
        """
        testbedList = []
        try:
            for testbed in self.collection.find():
                testbedList.append(testbed)
            return testbedList
        except errors as e:
            print("Error listing testbeds: %s", e)

    def gettByTitle(self, titleTestbed):
        """
        :param titleTestbed:
        :return:
        """
        try:
            self.collection.find_one({"title": titleTestbed})
        except errors as e:
            print("Error getting testbed by title: %s", e)

    def deletebyTitle(self, titleTestbed):
        """
        :param titleTestbed:
        :return:
        """
        try:
            self.collection.delete_one({titleTestbed})
        except errors as es:
            print("Error deleting a testbed by title: %s", e)