#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:31:44 2022

@author: devuser
"""

import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english2french(self):
        
        self.assertEqual(english_to_french("Hello").result["translations"][0]["translation"], 'Bonjour')
        self.assertNotEqual(english_to_french("Think").result["translations"][0]["translation"], 'Bonjour')

    def test_french2english(self):
        
        self.assertEqual(french_to_english("Bonjour").result["translations"][0]["translation"], 'Hello')
        self.assertNotEqual(french_to_english("Fille").result["translations"][0]["translation"], 'Hello')

    
if __name__ == '__main__':
    unittest.main()