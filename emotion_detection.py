import requests
import json

def emotion_detector(text_a_analizar):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_a_analizar } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    resultado = formatted_response['emotionPredictions'][0]['emotion'] 
    dominante = max(resultado, key=resultado.get)
    resultado["dominant_emotion"] = dominante

    return resultado