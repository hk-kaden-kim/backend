import os
import librosa
import soundfile as sf


def load_audio(audio_path:str):
    """
    ...

    Args:
        ...

    Returns:
        ...
    """
    # Load the audio
    try:
        audio, sr = librosa.load(audio_path, sr=16000)
        return audio, sr
    except Exception as e:
        print(f"Error loading {audio_path}: {str(e)}")
        return '', ''

def save_audio(audio_path:str, audio, sr):
    """
    ...

    Args:
        ...

    Returns:
        ...
    """
    format_to = '.wav'

    # Save the audio as .wav
    new_audio_path = os.path.splitext(audio_path)[0] + '_16k' + format_to
    # librosa.output.write_wav(new_audio_path, audio, sr)
    sf.write(new_audio_path, audio, sr)
    print(f"{audio_path}\nconverted to {format_to} and resampled to {sr} Hz.\nSaved as {new_audio_path}")

    return

def check_and_convert_audio(audio_path):
    """
    ...

    Args:
        ...

    Returns:
        ...
    """
    # Check if the file exists
    if not os.path.exists(audio_path):
        print(f"File {audio_path} does not exist.")
        return
    
    # Get the file extension
    _, ext = os.path.splitext(audio_path)

    # Check if the file is in .wav format
    if ext.lower() == ".wav":
        print(f"{audio_path} is already in .wav format.")

    # Convert the file into .wav with 16k sample rate.
    audio, sr = load_audio(audio_path)
    save_audio(audio_path, audio, sr)
    
    return

def get_audio_files_in_folder(folder_path):
    """
    Get a list of audio files (in .wav, .mp3, .flac, or .ogg format) in the specified folder.

    Args:
        folder_path (str): Path to the folder containing audio files.

    Returns:
        list: List of audio file paths.
    """
    audio_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in [".wav", ".mp3", ".flac", ".ogg"]:
                audio_files.append(os.path.join(root, file))
    return audio_files