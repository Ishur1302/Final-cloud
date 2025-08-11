import os
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ====== CONFIG ======
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"  # Path to unzipped Vosk model
SAMPLE_RATE = 16000  # 16 kHz required by most Vosk models
RECORD_SECONDS = 10  # Duration of recording in seconds

# Load model
if not os.path.exists(VOSK_MODEL_PATH):
    raise FileNotFoundError("Vosk model not found! Download and unzip from: https://alphacephei.com/vosk/models")

model = Model(VOSK_MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

# ====== CAPTURE AUDIO ======
print(f"🎙 Recording for {RECORD_SECONDS} seconds... Please speak clearly.")
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec_text = ""
    for _ in range(int(RECORD_SECONDS * SAMPLE_RATE / 8000)):
        data = q.get()
        if recognizer.AcceptWaveform(data):
            res = json.loads(recognizer.Result())
            rec_text += res.get("text", "") + " "
    res = json.loads(recognizer.FinalResult())
    rec_text += res.get("text", "")

print("📝 Transcription:", rec_text)

# ====== SENTIMENT ANALYSIS ======
sia = SentimentIntensityAnalyzer()
sentiment_scores = sia.polarity_scores(rec_text)

print("📊 Sentiment Scores:", sentiment_scores)

# Determine final label
if sentiment_scores['compound'] >= 0.05:
    sentiment = "Positive 😀"
elif sentiment_scores['compound'] <= -0.05:
    sentiment = "Negative 😞"
else:
    sentiment = "Neutral 😐"

print("💡 Final Sentiment:", sentiment)
