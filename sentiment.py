import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
recognizer = sr.Recognizer()

# Create a microphone instance (you can specify the index of the microphone you want to use)
microphone = sr.Microphone(device_index=0)  # Change the index as needed

# Function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

print("Listening...")

while True:
    try:
        with microphone as source:
            audio_data = recognizer.listen(source)  # Capture audio from the selected microphone
        text = recognizer.recognize_google(audio_data)
        sentiment = analyze_sentiment(text)

        print("You said: ", text)
        print("Sentiment: ", sentiment)
        break

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results: {0}".format(e))
