import speech_recognition as sr
import subprocess

def speak(text):
    subprocess.call(['say', '-vYuna', text])

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        audio = r.listen(source)

    try:
        transcript = r.recognize_google(audio, language="ko-KR")
        return transcript
    except sr.UnknownValueError:
        return "이해 할 수 없어요."
    except sr.RequestError as e:
        return e

if __name__ == "__main__":
    transcript = listen()
    speak(transcript)
    print(transcript)