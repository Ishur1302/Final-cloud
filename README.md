
# **Voice Sentiment Analysis Using IBM Watson**

## **Overview**
This project uses **IBM Watson AI services** to perform **voice sentiment analysis**.  
It captures audio (live or from file), transcribes it into text, and then analyzes the sentiment and emotional tone.  
It can classify speech as **Positive**, **Negative**, or **Neutral**, and provide emotion scores for improved decision-making.

***

## **Features**
- 🎤 **Speech-to-text** using IBM Watson Speech to Text
- 💬 **Sentiment & emotion analysis** using IBM Watson Natural Language Understanding
- 😊 Optional **Tone Analyzer** for more granular emotional tone detection
- ☁ **Cloud integration** with IBM Cloud Foundry or Kubernetes for deployment
- 💾 Stores audio and results in **IBM Cloud Object Storage** (optional)
- 📊 **Dashboard/report** for results display

***

## **Prerequisites**
Before running the project, make sure you have:
1. An **IBM Cloud account** ([https://cloud.ibm.com](https://cloud.ibm.com))
2. Created instances of:
   - **IBM Watson Speech to Text**
   - **IBM Watson Natural Language Understanding**
   - *(Optional)* IBM Watson Tone Analyzer
3. API keys and URLs for each service
4. Python 3.8+ installed on your system

***

## **Installation**
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/voice-sentiment-analysis.git
   cd voice-sentiment-analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate     # Mac/Linux
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your IBM Cloud credentials**
   Create a `.env` file in the project folder:
   ```
   SPEECH_TO_TEXT_APIKEY=your_speech_to_text_apikey
   SPEECH_TO_TEXT_URL=your_speech_to_text_url
   NLU_APIKEY=your_nlu_apikey
   NLU_URL=your_nlu_url
   TONE_APIKEY=your_tone_analyzer_apikey   # Optional
   TONE_URL=your_tone_analyzer_url         # Optional
   ```

***

## **Usage**
### **Run from terminal**
```bash
python main.py
```
1. Upload or record an audio file when prompted.
2. The program will:
   - Transcribe audio using **Speech to Text**
   - Analyze sentiment with **NLU**
   - (Optional) Perform tone analysis
3. Results are displayed on the console or sent to the dashboard.

***

## **Project Structure**
```
voice-sentiment-analysis/
│
├── main.py              # Main script for execution
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates for web interface
├── static/              # CSS/JS files
├── .env                 # IBM Cloud credentials (not version controlled)
└── README.md            # Project README
```

***

## **Deployment (IBM Cloud)**
1. Install the **IBM Cloud CLI**
   ```bash
   curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
   ```
2. Log in:
   ```bash
   ibmcloud login
   ```
3. Push the app to Cloud Foundry:
   ```bash
   ibmcloud target --cf
   ibmcloud cf push
   ```

***

## **Real-World Applications**
- **Customer Support** → Real-time emotional feedback for live agents
- **Market Research** → Voice survey analysis for product/brand insights
- **Mental Health Monitoring** → Detect emotional distress from speech

***

## **Acknowledgements**
- **IBM Watson** for AI-powered Speech to Text, Natural Language Understanding, and Tone Analyzer.
- **Flask** framework for building the web interface.

***

