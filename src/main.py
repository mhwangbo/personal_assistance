from speak_listen import listen, speak

if __name__ == "__main__":
    while True:
        transcript = listen().split()
        if transcript[0] == "안녕":
            speak("네, 안녕하세요.")