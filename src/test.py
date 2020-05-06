"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

def try_recording():
    import pyaudio
    import wave

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def get_audio_names():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def get_default_input():
    import pyaudio
    pa = pyaudio.PyAudio()
    print(pa.get_default_input_device_info())

if __name__ == "__main__":
    function_list = [get_default_input, get_audio_names, try_recording]
    while(True):
        print("1. Get Default Input")
        print("2. Get Audio Index Numbers")
        print("3. Try Recording From Microphone")
        print("999. Exit")
        try:
            select = int(input())
            if select == 999:
                break
            function_list[select - 1]()
        except:
            print("invalid option")
