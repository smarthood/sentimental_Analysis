import json
import streamlit as st
# from yt_extractor import get_video_info, get_audio_url
# from api_03 import save_transcript
# from gtts import gTTS
from pytube import extract
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from textblob import TextBlob


st.set_page_config(
    page_title="Sentimental Analysis",
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)
url = st.text_input('Enter video url', '')
if st.button('SUBMIT'):
    if 'youtube.com' not in url:
        st.write("Invalid url")
    else:
        st.write(f'({url}) is currently proccessing....')


if __name__ == "__main__":
    if (url != ""):
        id = extract.video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(id)
        formatter = TextFormatter()
        text_format = formatter.format_transcript(transcript)
        file = open('transcript.txt', w)
        file.write(text_format)
        blob = TextBlob(text_format)
        sentimental = blob.sentiment.polarity
        st.write(sentimental)
        print(sentimental)

        # audio = gTTS(text=text_format, lang="en", slow=False)
        # audio.save("transcript.wav")
        # save_transcript("transcript.wav", "senti_file", sentiment_analysis=True)
        # with open("data/iPhone_13.json", "r") as f:
        #     data = json.load(f)
        # positives = []
        # negatives = []
        # neutrals = []
        # for result in data:
        #     text = result["text"]
        #     if result["sentiment"] == "POSITIVE":
        #         positives.append(text)
        #     elif result["sentiment"] == "NEGATIVE":
        #         negatives.append(text)
        #     else:
        #         neutrals.append(text)

        # n_pos = len(positives)
        # n_neg  = len(negatives)
        # n_neut = len(neutrals)

        # print("Num positives:", n_pos)
        # print("Num negatives:", n_neg)
        # print("Num neutrals:", n_neut)

        # # ignore neutrals here
        # r = n_pos / (n_pos + n_neg)
        # print(f"Positive ratio: {r:.3f}")
