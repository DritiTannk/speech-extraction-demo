# speech-extraction-demo
_This project demonstrates how to extract text from video files_


### Python Libraries:
- moviepy = .0.3
- pydub = 0.25.1
- SpeechRecognition = 3.8.1

### Task Flow:

- Convert the video(.mp4) File To audio(.mp3) file.
- Convert audio(.mp3) file to audio(.wav) File 
- Extract text from the audio(.wav) File 
 
 
##### Installation steps:

1. Clone the repository
2. Create virtual enviornment

> virtualenv -p python3.6 venv_spech_ext_demo
>
> .venv_spech_ext_demo/bin/activate

3. Install dependencies/packages:

> pip install -r requirements.txt

4. Run the following scripts:

> python convertor.py
>
> python speech_extract.py


