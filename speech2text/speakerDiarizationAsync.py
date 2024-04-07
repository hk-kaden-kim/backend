from google.cloud import speech
import json
import os

def transcribe_gcs(gcs_uri: str) -> str:
    """Asynchronously transcribes the audio file specified by the gcs_uri.

    Args:
        gcs_uri: The Google Cloud Storage path to an audio file.

    Returns:
        The generated transcript from the audio file provided.
    """

    # ---------------------------------------------------------------------
    client = speech.SpeechClient.from_service_account_file('./key.json')

    # ---------------------------------------------------------------------
    audio = speech.RecognitionAudio(uri=gcs_uri)
    diarization_config = speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,
        min_speaker_count=2,
        max_speaker_count=6,
    )
    config = speech.RecognitionConfig(
        # encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, # For .wav with 16000 sampling rate
        sample_rate_hertz=48000, 
        language_code="en-US",
        diarization_config=diarization_config,
    )
    operation = client.long_running_recognize(config=config, audio=audio)

    # ---------------------------------------------------------------------
    print("Waiting for operation to complete...")
    response = operation.result(timeout=300)

    # ---------------------------------------------------------------------
    transcript_builder = []
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcript_builder.append({"Transcript": result.alternatives[0].transcript,
                                   "Confidence": result.alternatives[0].confidence})

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:
    result = response.results[-1]
    words_info = result.alternatives[0].words
    word_builder = []
    for word_info in words_info:
        word_builder.append({"Word":word_info.word,
                             "Speaker_tag":word_info.speaker_tag})    
        
    # ---------------------------------------------------------------------
    with open('transcript.json', 'w') as f:
        json.dump(transcript_builder, f, indent=4)
        transcript_filepath = os.path.abspath(f.name)

    with open('word_speaker_tag.json', 'w') as f:
        json.dump(word_builder, f, indent=4)
        word_tag_filepath = os.path.abspath(f.name)

    msg = f"File created!\n{transcript_filepath}\n{word_tag_filepath}"

    return msg



if __name__ == "__main__":
    # gcs_uri = "gs://talking-dataset/audio_1_English_Take_Away__Please_.mp3"
    # gcs_uri_wav = "gs://talking-dataset/business-meeting/biz-result-oup-brainstorming-meeting.wav"
    gcs_uri_mps = "gs://talking-dataset/business-meeting/biz-result-oup-brainstorming-meeting.mp3"
    msg = transcribe_gcs(gcs_uri_mps)
    print(msg)
