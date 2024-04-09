import json
import os
import gcp_speech2text as sp2txt

CREDENTIALS_FILE = "../gcp-credential/key.json"

if __name__ == "__main__":

    # gcs_uri_wav = "gs://talking-dataset/biz-meeting/biz-result-oup-brainstorming-meeting_16k.wav"
    # gcs_uri_wav = "gs://talking-dataset/biz-meeting/biz-result-oup-participating-in-meetings-1_16k.wav"
    # gcs_uri_wav = "gs://talking-dataset/biz-meeting/biz-result-oup-participating-in-meetings-2_16k.wav"
    gcs_uri_wav = "gs://talking-dataset/biz-meeting/biz-result-oup-team-meeting_16k.wav"

    # -------------------------------------------------------------------
    script_conf_pairs, word_tag_pairs = sp2txt.speech_to_text(gcs_uri_wav, CREDENTIALS_FILE)

    # -------------------------------------------------------------------
    with open('script_conf_pairs.json', 'w') as f:
        json.dump(script_conf_pairs, f, indent=4)
        filepath1 = os.path.abspath(f.name)
        
    with open('word_tag_pairs.json', 'w') as f:
        json.dump(word_tag_pairs, f, indent=4)
        filepath2 = os.path.abspath(f.name)

    print(f"Create Raw Files!\n{filepath1}\n{filepath2}\n")

    # -------------------------------------------------------------------
    transcript = sp2txt.generate_transcript_with_tag(word_tag_pairs)

    with open('transcript.json', 'w') as f:
        json.dump(transcript, f, indent=4)
        filepath3 = os.path.abspath(f.name)
    
    print(f"Create Transcript File!\n{filepath3}\n")