def voice_recognize():
    import pyaudio
    import wave
    import keyboard
    import speech_recognition as sr

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                       channels = CHANNELS,
                       rate = RATE,
                       input = True,output = False,
                       input_device_index = 0,
                       frames_per_buffer=CHUNK)
    while True:
        try:
            print("recording... to record press c , to quit press q")
            frames = []
            while True:
                if keyboard.is_pressed('c'):
                    data = stream.read(CHUNK)
                    frames.append(data)
                if keyboard.is_pressed('q'):
                    break
            print("finished recording")
            stream.stop_stream()
            stream.close()
            audio.terminate()
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()
            r = sr.Recognizer()
            harvard = sr.AudioFile('file.wav')
            with harvard as source:
                audio = r.record(source)
            return r.recognize_google(audio)
        except Exception:
            return 'no input'