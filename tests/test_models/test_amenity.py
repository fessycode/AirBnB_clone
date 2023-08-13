#!/usr/bin/env python3
"""
A unit test module for testing ``models/amenity.py`` module.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class Test_Amenity(unittest.TestCase):
    """
    Test the basic features of the Amenity class.
    """

    def test_instance_uuid_is_unique(self):
        """
        This test method verifies that the instance UUID is unique.
        """
        user1 = Amenity()
        user2 = Amenity()
        self.assertNotEqual(user1.id, user2.id)

    def test_instance_created_at_is_str(self):
        """
        This test method confirms that the created_at instance
        attribute is a string.
        """
        user1 = Amenity()
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_save_method(self):
        """
        This method of this test class tests if:
        save method is working as expected.
        """
        from time import sleep
        user1 = Amenity()
        sleep(2)
        user1.save()
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_string_representation(self):
        """
        This method of this test class tests if:
        string representation is presented as required.
        """
        user1 = Amenity()
        string = "[{}] ({}) {}".format(user1.__class__.__name__,
                                       user1.id, user1.__dict__)
        self.assertEqual(user1.__str__(), string)

    def test_instance_dictionary(self):
        """
        This test method ensures that the instance dictionary
         is updated as expected.
        """
        user1 = Amenity()
        user1.name = "betty"
        self.assertTrue("__class__" in user1.to_dict())
        self.assertTrue("name" in user1.to_dict())

    def test_new_instance_from_dictionary(self):
        """
        This method of this test class tests if:
        a new instance can be created from a dictionary.
        """
        user1 = Amenity()
        model_json = user1.to_dict()
        user2 = Amenity(**model_json)
        self.assertFalse(user1 is user2)

    def test_new_instance_datetime_variables(self):
        """
        This test method verifies that the datetime
        variables of instances remain unchanged.
        """
        user1 = Amenity()
        model_json = user1.to_dict()
        user2 = Amenity(**model_json)
        self.assertEqual(type(user2.created_at), datetime)
        self.assertEqual(type(user2.updated_at), datetime)

    def test_new_instance_properties_against_old(self):
        """
        This test method checks whether properties of a new
        instance match those of an older instance.
        """
        user1 = Amenity()
        user1.name = "New_Instance"
        model_json = user1.to_dict()
        user2 = Amenity(**model_json)
        self.assertEqual(type(user1), type(user2))
        self.assertEqual(user1.id, user2.id)
        self.assertEqual(user1.name, user2.name)
