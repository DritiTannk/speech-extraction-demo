import os
import glob

import speech_recognition as sr

if __name__ == '__main__':
    i_path = './output/'

    if os.path.exists(i_path):
        i_path = i_path + '*'
        for file in glob.glob(i_path):
            file_name = os.path.basename(file)
            name, ext = os.path.splitext(file_name)

            if ext == '.wav':
                print(f'\n\n File Name is: {name}')
                AUDIO_FILE = file
                r = sr.Recognizer()  # Speech recognition  object

                with sr.AudioFile(AUDIO_FILE) as source:
                    audio = r.record(source)  # Audio extract
                    text = r.recognize_google(audio)  # Speech extract from the audio file
                    print("\n\n Transcription: ", text)
            else:
                print(f'\n\n Inappropriate File Format For File --> {file_name} !!!')

