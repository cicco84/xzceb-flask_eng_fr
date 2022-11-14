import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey=os.environ['apikey']
url = os.environ['url']
version_lt = '2018-05-01'

authenticator  = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(authenticator=authenticator, version=version_lt)
lang_translator.set_service_url(url)
def englishToFrench(englishText):
    return (lang_translator.translate(text=englishText,model_id='en-fr'))

def frenchToEnglish(frenchText):
    return (lang_translator.translate(text=frenchText,model_id='fr-en'))

if __name__ == "__main__":
    print(englishToFrench("Hello"))