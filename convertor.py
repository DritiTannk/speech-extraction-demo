import os
import glob

import moviepy.editor as mp
from pydub import AudioSegment


def mp4_convertor(file_path, f_name):
    """
    Converts video(.mp4) file to audio(.mp3) file.
    """
    o_file_name = f_name + '_converted.mp3'
    o_path = 'output/' + o_file_name

    clip = mp.VideoFileClip(file_path)  # Reading the video file
    clip.audio.write_audiofile(o_path)  # Extracting and writing audio
    print('\n\n Video File (.mp4) Conversion Completed !!!')
    mp3_converter(o_path, f_name)


def mp3_converter(audio_fpath, f_name):
    """
    Converts audio(.mp3) file to audio(.wav) file.
    """
    o_file_name = f_name + '_transcrib.wav'
    o_path = 'output/' + o_file_name

    sound = AudioSegment.from_mp3(audio_fpath)  # Extracting audio from the .mp3 file_path
    sound.export(o_path, format="wav")

    print('\n\n Audio File (.mp3) conversion completed !!!')


if __name__ == '__main__':
    i_path = './input/'

    if os.path.exists(i_path):
        i_path = i_path + '*'
        for file in glob.glob(i_path):
            file_name = os.path.basename(file)
            name, ext = os.path.splitext(file_name)

            if ext == '.mp4':
                mp4_convertor(file, name)
    else:
        print('\n\n Invalid Path OR Something Went Wrong !!!')
