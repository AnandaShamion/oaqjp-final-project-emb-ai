''' 
server.py
Emotion detection Flask application from text input.
'''
#import Flask and emotion_detector function
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''This code recieves text from the HTML interface and 
    runs emotion detection using the emotion_detector function.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:#additional code for error handling
        return "Invalid text! Please try again."
    # display string
    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
        f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    '''This function initiates the rendering of the main application page over the Flask channel'''
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
