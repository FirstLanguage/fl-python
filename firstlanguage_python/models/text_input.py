# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from firstlanguage_python.models.input import Input
import os
from firstlanguage_python.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError
from firstlanguage_python.api_helper import APIHelper


class TextInput(object):

    """Implementation of the 'TextInput' model.

    TODO: type model description here.

    Attributes:
        input (Input): Direct Text Input

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "input": 'input'
    }

    def __init__(self,
                 input=None):
        """Constructor for the TextInput class"""

        # Initialize members of the class
        self.input = input

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        input = Input.from_dictionary(dictionary.get('input')) if dictionary.get('input') else None

        # Return an object of this model
        return cls(input)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
