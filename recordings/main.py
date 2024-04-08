import recordings as rec

if __name__ == "__main__":

    folders = "../dataset/monologue/"
    audio_files = rec.get_audio_files_in_folder(folders)

    for f in audio_files:
        rec.check_and_convert_audio(f)
        print()
