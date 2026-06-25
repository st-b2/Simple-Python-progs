import speech_recognition as sr
import os

def recognize_speech(audio_file, language='ru-RU'):
    if not os.path.exists(audio_file):
        print(f"[!] Ошибка: Файл '{audio_file}' не найден")
        return None
    
    r = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file) as source:
            print(f"[*]Обработка файла: {audio_file}")
            audio = r.record(source)
        
        print("[*]Распознавание речи...")
        text = r.recognize_google(audio, language=language)
        return text
        
    except sr.UnknownValueError:
        print("[!]Google Speech Recognition не смог распознать аудио")
        return None
        
    except sr.RequestError as e:
        print(f"[!]Ошибка при запросе к Google Speech Recognition: {e}")
        return None
        
    except Exception as e:
        print(f"[!]Ошибка: {e}")
        return None

# ==========

FILE_PATH = 'audio.wav'  
LANGUAGE = 'ru-RU'       


result = recognize_speech(FILE_PATH, LANGUAGE)

if result:
    print("\n" + "="*50)
    print("[!]Распознанный текст:")
    print("="*50)
    print(result)
    print("="*50)
    
    # сохранить в файл 
    # with open('result.txt', 'w', encoding='utf-8') as f:
    #     f.write(result)