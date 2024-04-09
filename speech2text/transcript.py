import os
import json

def map_speaker_tag(transcript:dict, speaker:list) -> dict:
    tag = []

    for tr in transcript:
        if tr['Speaker'] not in tag:
            tag.append(tr['Speaker'])
    assert len(tag) == len(speaker), "item counts are different!"
    speaker_tag = dict(zip(tag, speaker))

    print(f"Mapped speaker's name into the tag!")
    return speaker_tag

def convert_transcript_json2txt(transcript_json:dict, speaker:list) -> str:
    transcript_txt = ''

    speaker_tag = map_speaker_tag(transcript_json, speaker)

    for tr in transcript_json:
        speaker = speaker_tag[tr['Speaker']]
        content = tr['Contents']
        transcript_txt += f"{speaker}:\n{content}\n\n"

    print(f"Converted transcript json into txt! {len(transcript_txt)}")
    return transcript_txt

def save_result(filename:str, contents) -> str:

    _, ext = os.path.splitext(filename)

    if ext.lower() == ".json":
        with open(filename, 'w') as f:
            json.dump(contents, f, indent=4)

    elif ext.lower() == ".txt":
        with open(filename, "w") as f:
            f.write(contents)
    
    print(f"Saved contents into the file! \n{filename}")
    return 