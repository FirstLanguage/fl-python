# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import os
from firstlanguage_python.utilities.schema_validator_wrapper import SchemaValidatorWrapper
from jsonschema import ValidationError
from firstlanguage_python.api_helper import APIHelper


class Input4(object):

    """Implementation of the 'Input4' model.

    TODO: type model description here.

    Attributes:
        text (string): Word or sentence or a paragraph. Special characters
            will not be stripped.
        lang (string): Allowed ISO language code. Refer languages section.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "text": 'text',
        "lang": 'lang'
    }

    def __init__(self,
                 text=None,
                 lang=None):
        """Constructor for the Input4 class"""

        # Initialize members of the class
        self.text = text
        self.lang = lang

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
        text = dictionary.get('text')
        lang = dictionary.get('lang')

        # Return an object of this model
        return cls(text,
                   lang)

    @classmethod
    def validate(cls, val):
        """Validates value against class schema

        Args:
            val: the value to be validated

        Returns:
            boolean : if value is valid against schema.

        """
        return SchemaValidatorWrapper.getValidator(APIHelper.get_schema_path(os.path.abspath(__file__))).is_valid(val)
