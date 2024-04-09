from google.cloud import speech

def speech_to_text(gcs_uri: str, credentials: str):
    """Asynchronously transcribes the audio file specified by the gcs_uri.

    Args:
        ...

    Returns:
        ...
    """

    # ---------------------------------------------------------------------
    client = speech.SpeechClient.from_service_account_file(credentials)

    # ---------------------------------------------------------------------
    audio = speech.RecognitionAudio(uri=gcs_uri)
    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=7,
    )
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, # For .wav with 16000 sampling rate
        sample_rate_hertz=16000, 
        language_code="en-US",
        diarization_config=diarization_config,
    )
    operation = client.long_running_recognize(config=config, audio=audio)

    # ---------------------------------------------------------------------
    print("Waiting for operation to complete...\n")
    response = operation.result(timeout=300)

    # ---------------------------------------------------------------------
    script_conf_pairs = []
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        script_conf_pairs.append({"Transcript": result.alternatives[0].transcript,
                                   "Confidence": result.alternatives[0].confidence})

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]
    words_info = result.alternatives[0].words
    word_tag_pairs = []
    for word_info in words_info:
        word_tag_pairs.append({"Word":word_info.word,
                             "Speaker_tag":word_info.speaker_tag})    

    return script_conf_pairs, word_tag_pairs



def generate_transcript_with_tag(word_tag_pairs):

    words = [w_t['Word'] for w_t in word_tag_pairs]
    tags = [w_t['Speaker_tag'] for w_t in word_tag_pairs]

    current = 0
    sentence = []
    transcript = []
    for i, t in enumerate(tags):
        if i == 0:
            current = t
            sentence.append(words[i])
            continue
        if current != t:
            transcript.append({"Speaker":current, "Contents":' '.join(sentence)})
            current, sentence = t, [words[i]]
        else:
            sentence.append(words[i])
    
    return transcript