#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:04:23 2022

@author: devuser
"""

from flask import Flask
from translator import english_to_french, french_to_english

app = Flask("Cicco Translator")

@app.route("/english_to_french/<text>")
def english_to_french_translate(text):
    return english_to_french(text).result["translations"][0]["translation"]

@app.route("/french_to_english/<text>")
def french_to_english_translate(text):
    return french_to_english(text).result["translations"][0]["translation"]



if __name__=="__main__":
    app.run(debug=True)
    