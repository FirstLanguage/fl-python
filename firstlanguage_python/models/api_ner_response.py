# -*- coding: utf-8 -*-

"""
firstlanguage

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiNerResponse(object):

    """Implementation of the 'Api Ner Response' model.

    TODO: type model description here.

    Attributes:
        entity_group (string): Entity group inferred.
        word (string): Corresponding word
        start (string): Start position of the entity in the given input.
        end (string): Start position of the entity in the given input.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_group": 'entity_group',
        "word": 'word',
        "start": 'start',
        "end": 'end'
    }

    def __init__(self,
                 entity_group=None,
                 word=None,
                 start=None,
                 end=None):
        """Constructor for the ApiNerResponse class"""

        # Initialize members of the class
        self.entity_group = entity_group
        self.word = word
        self.start = start
        self.end = end

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
        entity_group = dictionary.get('entity_group')
        word = dictionary.get('word')
        start = dictionary.get('start')
        end = dictionary.get('end')

        # Return an object of this model
        return cls(entity_group,
                   word,
                   start,
                   end)