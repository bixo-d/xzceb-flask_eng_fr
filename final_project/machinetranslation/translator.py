"""
Module translator.py
    Contains the functions for translating english to french and viceversa
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-06-21',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function for translating an english string to french
        if the string is empty, it catches the exception and returns None
    """
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text=translation['translations'][0]['translation']
    except ValueError:
        return None
    return french_text

def french_to_english(french_text):
    """
    Function for translating an french string to english
        if the string is empty, it catches the exception and returns None
    """
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text=translation['translations'][0]['translation']
    except ValueError:
        return None
    return english_text
