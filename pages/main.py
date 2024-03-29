import json
import streamlit as st
from pytube import extract
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from textblob import TextBlob
import time


st.set_page_config(
    page_title="Sentimental Analysis",
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)
st.image('url.png')
url = st.text_input('Enter video url', '')
if st.button('SUBMIT'):
    if 'youtube.com' not in url:
        st.write("Invalid url")


if __name__ == "__main__":
    if (url != ""):
        id = extract.video_id(url)
        transcript = YouTubeTranscriptApi.get_transcript(id)
        formatter = TextFormatter()
        text_format = formatter.format_transcript(transcript)
        file = open('transcript.txt', "w")
        file.write(text_format)
        blob = TextBlob(text_format)
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.05)
            progress_bar.progress(i+1)
        progress_bar.empty()
        sentimental = blob.sentiment.polarity
        image = 'nutral.png'
        print(type(sentimental))
        if sentimental < 0.1:
            sentimental = -sentimental
            image = 'red.png'
        else:
            image = 'green.png'
        perc = str(round(sentimental/1 * 100))+"%"
        st.metric("sentimental value", str(sentimental), perc)
        st.image(image)
        print(sentimental)
