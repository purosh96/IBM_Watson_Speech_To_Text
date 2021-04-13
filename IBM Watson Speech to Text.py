#!/usr/bin/env python
# coding: utf-8

#install ibm_watson and ibm_cloud_sdk_core using PIP
from ibm_watson import SpeechToTextV1 as sttv1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Get your own API url and key https://cloud.ibm.com/catalog/services/speech-to-text
url_sttv1 = "Pass the URL here"
key_sttv1 = IAMAuthenticator("asfiiiPASSYOURKEYiiiMiP")

s2t = sttv1(authenticator=key_sttv1)
s2t.set_service_url(url_sttv1)
myPath = "C:\\Users\\Downloads\\audio-file.flac"

with open(myPath,"rb") as audiofile:
    result = s2t.recognize(audio = audiofile, content_type= "audio/flac")
result.result['results'][0]



