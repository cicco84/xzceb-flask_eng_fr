"""
Module for Courser final exam
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey=os.environ['apikey']
url = os.environ['url']
VERSION_LT = '2018-05-01'

authenticator  = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(authenticator=authenticator, version=VERSION_LT)
lang_translator.set_service_url(url)
def english_to_french(english_text):
    result = lang_translator.translate(text=english_text,model_id='en-fr')
    return result

def french_to_english(french_text):
    result = lang_translator.translate(text=french_text,model_id='fr-en')
    return result

if __name__ == "__main__":
    print(english_to_french("Hello").result["translations"][0]["translation"])
    print(french_to_english("Bonjour").result["translations"][0]["translation"])
    