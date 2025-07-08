from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    # docstring
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    # docstring
    text_to_analyze = request.args.get('textToAnalyze')

    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return "For the given statement, the system response is " + \
        f"'anger': {res['anger']}, 'disgust': 0.{res['disgust']}, 'fear': 0.{res['fear']}," + \
        " 'joy': 0.{res['joy']} and 'sadness': 0.{res['sadness']}. " + \
        f"The dominant emotion is {res['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
