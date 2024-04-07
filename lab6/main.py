import wave
import pyaudio
import subprocess
import webbrowser
import whisper
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy3

def start_sream(path, name):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    
    with wave.open(path + name, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')
        
        stream.close()
        p.terminate()

def recognize():
    model = whisper.load_model("base")
    result = model.transcribe(path + name)
    return result["text"]

def tokenization():
    corpus = [] 
    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('russian'))
    morph = pymorphy3.MorphAnalyzer()
    
    text = recognize()
    tokens = word_tokenize(text)
    tokens = [morph.parse(token)[0].normal_form for token in tokens if token.isalnum() and not token.isdigit()]
    tokens = [token for token in tokens if token not in stop_words]
    text = ' '.join(tokens)
    corpus.append(text)
    return corpus

def set_command():
    
    words_for_web = ['поиск', 'повиск', 'оиск', 'пуиск', 'уиск', 'пойск', 'ойск', 'найти', 'наити', 'найди',
                     'poisk', 'oisk', 'puisk', 'uisk' ,'naiti', 'search']
    words_for_video = ['youtube', 'ютуб', 'видео', 'водос', 'видосик',
                       'video, vidos, vidosik']
    steam = ['стим','стиль','штим','stim','stem']
    code = ['vscode','code','виэскод','вскод','код','вижуал']
    
    corpus = tokenization()
    print('\nПолучен корпус слов:', corpus)    

    corpus = str(corpus).replace("['", "").replace("']", "").split(' ')
    
    to_web = False
    to_video = False
    is_steam = False
    is_code = False
    
    # Удаление ключего слова из поиска 
    replace_corpus = []
    for i in corpus: 
        if i in words_for_web:
            to_web = True
        elif i in words_for_video:
            to_video = True
            
        elif i in steam:
            is_steam = True   
        elif i in code:
            is_code = True             
            
        else:    
            replace_corpus.append(i)
            
    if to_web == True:
        print('Переход в браузер ...')
        webbrowser.open('https://yandex.ru/search/?text=' + str(replace_corpus).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))            
        
    elif to_video == True:
        print('Открываю видеохостинг youtube ...')
        webbrowser.open('https://www.youtube.com/results?search_query=' + str(replace_corpus).replace("[", "").replace("]", "").replace("'", "").replace(",", "")) 
        
    elif is_steam == True:
        print('Открываю локальное прилажение steam ...')
        subprocess.call('steam')
    
    elif is_code == True:
        print('Открываю локальное прилажение VScode...')
        subprocess.call('code')
        
    else:
        print('\nКлючевого слова не найдено, повторите попытку!\n')
        
if __name__ == '__main__':
    
    path = '/home/kirill/projects/Methods-and-algorithms-for-weakly-structured-data/Methods-and-algorithms-for-weakly-structured-data/lab6/'
    name = 'output.wav'
    
    print('\nПрограмма поддерживает 3 вида комманд: 1) открыть браузер и найти что-нибудь в поисковике, 2) поиск видео из yotube, 3) запуск программ на ПК(можно открыть 2 программы: vscode и стим)')
    print('\nКлючевые слова для 1 команды: поиск, найти')
    print('\nКлючевые слова для 2 команды: youtube, видео')
    print('\nКлючевые слова для 3 команды: steam, code')
    print('\nПроизнесите комманду в течении 5 секунд:\n')
    
    start_sream(path, name) 
    set_command()
    
    