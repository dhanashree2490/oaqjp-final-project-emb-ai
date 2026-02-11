''' Executing this function initiates the application of Emotion Detection
    to be executed over the Flask channel and deployed on
    localhost:5001.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Function printing the dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")
 # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    result = (
        "For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} "
        f"and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
