import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    emotion_data= formatted_response['emotionPredictions'][0]
    anger_score = emotion_data['emotion']['anger']
    disgust_score = emotion_data['emotion']['disgust']
    fear_score = emotion_data['emotion']['fear']
    joy_score = emotion_data['emotion']['joy']
    sadness_score = emotion_data['emotion']['sadness']

    emotion_scores = emotion_data['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
