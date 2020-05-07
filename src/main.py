import speech_recognition as sr
import subprocess

def speak(text):
    subprocess.call(['say', '-vYuna', text])

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening...")
        audio = r.listen(source)
        print("finished")

    try:
        transcript = r.recognize_google(audio, language="ko-KR")
    except sr.UnknownValueError:
        transcript = "죄송해요, 못 알아 들었어요"
    except sr.RequestError:
        transcript = "오류가 발생했습니다"
    return transcript

if __name__ == "__main__":
    transcript = listen()
    print(transcript.split())