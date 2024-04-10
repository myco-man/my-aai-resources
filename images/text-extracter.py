from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.core.exceptions import HttpResponseError
import requests
 # import namespaces
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

pdf_file = 'images/Kolendo.Resume.pdf'


def main():
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        cv_client = ImageAnalysisClient(
                endpoint=ai_endpoint,
                credential=AzureKeyCredential(ai_key))
        try:
            result = cv_client.analyze(
            image_url=pdf_file,
            visual_features=[VisualFeatures.READ])

        except Exception as ex:
            print(ex)