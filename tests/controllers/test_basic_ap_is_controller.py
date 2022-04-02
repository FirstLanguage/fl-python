# -*- coding: utf-8 -*-

"""
firstlanguageapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.requestdeserialization.deserialize_basic_ap_is_controller import BasicApIs
from tests.http_response_catcher import HttpResponseCatcher
from firstlanguageapi.api_helper import APIHelper
from firstlanguageapi.controllers.basic_ap_is_controller import BasicAPIsController


class BasicAPIsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(BasicAPIsControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = BasicAPIsController(cls.config, cls.auth_managers, cls.response_catcher)

    # # Stemmer : Defintion and it's usage
    #A word takes different inflectional forms. For instance, the word, "Compute" can take the forms, "computing", "computation",  and "computerize". The NLP applications such as Search Engines and Information Extraction would want to store the base or stem of the word, i.e "Compute" instead of accomodating all its inflected forms. This will yield in dimensionality reduction and incerases the efficiency of the system. The stemmer cuts the prefix and suffix of a word. 
    #
    # # Languages covered:
    #  Our stemmer works for the following  26 languages. 
    #  
    #| Languages    | ISO Code   |
    #|--------------|------------|
    #|  Arabic      |  ar        |
    #|  Catalan     |  ca        |
    #|  Danish      |  da        |
    #|  German      |  de        |
    #|  Greek       |  el        |
    #|  English     |  en        |
    #|  Spanish     |  es        |
    #|  Basque      |  eu        |
    #|  Finnish     |  fi        |
    #|  French      |  fr        |
    #|  Irish       |  ga        |
    #|  Hindi       |  hi        |
    #|  Hungarian   |  hu        |
    #|  Indonesian  |  id        |
    #|  Italian     |  it        |
    #|  Lithuanian  |  lt        |
    #|  Nepali      |  ne        |
    #|  Dutch       |  nl        |
    #|  Norwegian   |  no        |
    #|  Portuguese  |  pt        |
    #|  Romanian    |  ro        |
    #|  Russian     |  ru        |
    #|  Serbian     |  sr        |
    #|  Swedish     |  sv        |
    #|  Tamil       |  ta        |
    #|  Turkish     |  tr        |
    #
    def test_get_stemmer(self):
        # Parameters for the API call
        body = BasicAPIs.deserialize_getStemmer('{"input":{"text":"அவள் வேகமாக ஓடினாள்","lang":"ta"}}')

        # Perform the API call through the SDK function
        result = self.controller.get_stemmer(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"originalText":"அவள்","stem":"அவள்"},{"originalText":"வேகமாக","ste'
            'm":"வேகம்"},{"originalText":"ஓடினாள்","stem":"ஓடி"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

    # # Lemmatizer : Defintion and it's usage
    #
    #Lemmatizer is similar to stemmer that gives the stemmed version of a word but lemmatizer differs from the stemmer in giving a meaningful stem or the lemma. For instance, for the word, "smiling", the stemmer would give, "smil", stemming the suffix, "ing" but the lemmatizer would give the meaningful stem, "smile". lemmatizers can be used in applications such as,  Machine Translation, Search Engines, Text Summarization etc.
    #
    ## Languages covered:
    #| Languages          | ISO Code |
    #|--------------------|----------|
    #| Catalan            | ca       |
    #| Danish             | da       |
    #| Dutch              | nl       |
    #| English            | en       |
    #| French             | fr       |
    #| German             | de       |
    #| Greek              | el       |
    #| Italian            | it       |
    #| Lithuanian         | lt       |
    #| Macedonian         | mk       |
    #| Norwegian (Bokmål) | nb       |
    #| Polish             | pl       |
    #| Portuguese         | pt       |
    #| Romanian           | ro       |
    #| Russian            | ru       |
    #| Spanish            | es       |
    #
    #
    #
    #
    def test_get_lemma(self):
        # Parameters for the API call
        body = BasicAPIs.deserialize_getLemma('{"input":{"text":"Smiling makes everyone happy","lang":"en"}}')

        # Perform the API call through the SDK function
        result = self.controller.get_lemma(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"originalText":"Smiling","lemmatized":"smile"},{"originalText":"ma'
            'kes","lemmatized":"make"},{"originalText":"everyone","lemmatized":"'
            'everyone"},{"originalText":"happy","lemmatized":"happy"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

    # # Morphological Analyzer : Defintion and it's usage
    #Morphological Analyzer analyzes how a word is formed. It breaks a word into smaller units called, "morphemes" and gives a clue on the pattern of words of a particular langauge.  It can be used for building applications such as,  Machine Translation, Text Summarization, Search systems etc. 
    #
    #
    ## Languages covered:
    #| Languages          | ISO Code |
    #|--------------------|----------|
    #| Catalan            | ca       |
    #| Danish             | da       |
    #| Dutch              | nl       |
    #| English            | en       |
    #| French             | fr       |
    #| German             | de       |
    #| Greek              | el       |
    #| Italian            | it       |
    #| Japanese           | ja       |
    #| Lithuanian         | lt       |
    #| Macedonian         | mk       |
    #| Norwegian (Bokmål) | nb       |
    #| Polish             | pl       |
    #| Portuguese         | pt       |
    #| Russian            | ru       |
    #| Spanish            | es       |
    #
    def test_get_morph(self):
        # Parameters for the API call
        body = BasicAPIs.deserialize_getMorph('{"input":{"text":"Let us begin the API development.","lang":"en"}}'
            '')

        # Perform the API call through the SDK function
        result = self.controller.get_morph(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('{"Let":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["Sing"],"Perso'
            'n":["1"],"PronType":["Art"],"Definite":["Def"],"NounType":["Prop"]'
            '},"us":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["Sing"],"Perso'
            'n":["1"],"PronType":["Art"],"Definite":["Def"],"NounType":["Prop"]'
            '},"begin":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["Sing"],"Pe'
            'rson":["1"],"PronType":["Art"],"Definite":["Def"],"NounType":["Pro'
            'p"]},"the":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["Sing"],"P'
            'erson":["1"],"PronType":["Art"],"Definite":["Def"],"NounType":["Pr'
            'op"]},"API":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["Sing"],"'
            'Person":["1"],"PronType":["Art"],"Definite":["Def"],"NounType":["P'
            'rop"]},"development":{"VerbForm":["Inf"],"Case":["Acc"],"Number":['
            '"Sing"],"Person":["1"],"PronType":["Art"],"Definite":["Def"],"Noun'
            'Type":["Prop"]},".":{"VerbForm":["Inf"],"Case":["Acc"],"Number":["'
            'Sing"],"Person":["1"],"PronType":["Art"],"Definite":["Def"],"NounT'
            'ype":["Prop"]}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))

    #  # Parts of Speech Tagger : Defintion and it's usage
    #  Parts of Speech Tagger, which is shortly known as POS Tagger is a software that automatically finds the word classes, when a text input is given. The text input can be a word, a sentence or a set of sentences. The word classes are the grammatical categories such as, Noun, Verb, Adverb etc. The category assigned to each word is called as a tag. A set of tags, each indicating a grammatical category is called, "tagsets". POS tagging is a mandatory pre-processing for most of the Natural Language Processing Applications such as, Information Extraction, Information Retreival systems and Summary generation systems. A POS Tagger is a language-dependent software as the grammar rules will differ for every language. For instance, a word ending with "ing" might indicate a "Verb" in English but this will not be applicable for other languages. 
    #
    #
    ## Languages covered:
    #
    #| Languages          | ISO Code |
    #|--------------------|----------|
    #| Chinese            | zh       |
    #| Dutch              | nl       |
    #| English            | en       |
    #| German             | de       |
    #| Italian            | it       |
    #| Lithuanian         | lt       |
    #| Polish             | pl       |
    #| Romanian           | ro       |
    #| Tamil              | ta       |
    # 
    #
    #
    def test_get_postag(self):
        # Parameters for the API call
        body = BasicAPIs.deserialize_getPostag('{"input":{"text":"Let us begin the API development.","lang":"en"}}'
            '')

        # Perform the API call through the SDK function
        result = self.controller.get_postag(body)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize('[{"originalText":"Let","postag":"VERB"},{"originalText":"us","postag'
            '":"PRON"},{"originalText":"begin","postag":"VERB"},{"originalText":"'
            'the","postag":"DET"},{"originalText":"API","postag":"PROPN"},{"orgi'
            'nalText":"development","postag":"NOUN"},{"originalText":".","postag'
            '":"PUNCT"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))
