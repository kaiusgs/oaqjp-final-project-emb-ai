import requests
import json 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }

    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        res_text = json.loads(response.text) 
        emotions = res_text["emotionPredictions"][0]["emotion"]

        dominant_emotion = ''
        dominant_emotion_score = -1
        for em in emotions:
            if( emotions[em] > dominant_emotion_score ):
                dominant_emotion_score = emotions[em]
                dominant_emotion = em 

        emotions["dominant_emotion"] = dominant_emotion

    elif response.status_code == 400:
        emotions = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    return emotions

# print(emotion_detector("I love this new technology."))