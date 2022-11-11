import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey=os.environ['apikey']
url = os.environ['url']
version_lt = '2018-05-01'
def englishToFrench(englishText):
    eng_french_translator = LanguageTranslatorV3(iam_apikey=apikey, url=url, version=version_lt)
    return (eng_french_translator.translate(text=englishText),model_id='en-fr')

def frenchToEnglish(frenchText):
    french_eng_translator = LanguageTranslatorV3(iam_apikey=apikey, url=url, version=version_lt)
    return (french_eng_translator.translate(text=frenchText),model_id='fr-en')

