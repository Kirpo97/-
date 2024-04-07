import wave
import time
import threading
import tkinter
import pyaudio
import whisper

class Voice_commander():
    
    def __init__(self):
        self.root = tkinter.Tk()
        
        self.path = '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab6/'
        self.name = 'out.wav'
        
        self.root.title("Голосовой помошник")
        self.root.geometry("250x200")
        self.root.resizable(False, True)
        
        self.button = tkinter.Button(
            text = 'Старт',
            font = ('Arial', 20, 'bold'),
            command=self.click_handler
        )
        self.com_text = tkinter.Label(
            text='',
            font = ('Arial', 20)
            )
        
        self.recording = False
        self.button.pack()
        self.com_text.pack() 

        self.root.mainloop()
        
    def click_handler(self):
        if self.recording:
            self.recording = False
        else:
            self.recording = True
            threading.Thread(target=self.record).start()
            self.button["text"] = 'Стоп'
            
    
    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
            input_device_index=20
        )
        frames = []
        start = time.time()
        
        while self.recording:
            data = stream.read(1024, exception_on_overflow=False)
            frames.append(data)
            
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
            hours = mins // 60
            self.com_text.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
            
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        path = '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab6/'
        name = 'out.wav'
        
        sound_file = wave.open(path + name, 'wb')
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
        
        self.recognize(self.path, self.name)



    def recognize(self):
        model = whisper.load_model("base").detect_language
        
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(self.path + self.name)
        audio = whisper.pad_or_trim(audio)
        
        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(self.audio).to(model.device)
        
        # detect the spoken language
        _, probs = self.model.detect_language()
        print(f"Detected language: {max(probs, key=probs.get)}")
        
        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)

        # print the recognized text
        print(result.text)
    
    

if __name__ == '__main__':
  
    path = '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab6/out.wav'
    name = 'out.wav'
    
    v = Voice_commander()
        