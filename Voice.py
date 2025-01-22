import streamlit as st
import speech_recognition as sr

def whisper_transcribe(_,_1):
    return "Transcription with whisper not implemented."

def transcribe_speech(api_choice,language) :

    r = sr.Recognizer()
    with sr.Microphone() as source :

        st.info("Speak Now...")
        audio_text = r.listen(source)
        st.info("Transcription...")

        try :
            if api_choice == "Google":

                text = r.recognize_google(audio_text,language = language)

            elif api_choice == "Whisper":
                text = whisper_transcribe(audio_text,language)
            else :
                return "API not supported."
            return text
        except sr.UnknownValueError:
            return "Sorry, I don't Understand."

        except sr.RequestError as e:
            return f"Error de service : {e}"


def save_transcription(text):

    with open("transcription.txt", "w",encoding="utf-8") as f:
        f.write(text)

def main() :

    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    api_choice = st.selectbox("Choose Speech Recognition API:",
                              ["Google", "Whisper"])
    language = st.selectbox("Choose language:", ["fr-FR", "en-US"])

    if st.button("Start Recording"):
        text = transcribe_speech(api_choice, language)
        st.write("Transcription : " , text)

        if st.button("Save transcription"):
            save_transcription(text)
            st.success("save transcription in transcription.txt")

if __name__ == "__main__" :
    main()