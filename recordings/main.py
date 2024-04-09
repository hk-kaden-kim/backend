import os
import recordings as rec
import gcp_bucket as bucket

BUCKET_NAME = "talking-dataset"
DESTINATION_BLOB_NAME = "uploaded-file.txt"
CREDENTIALS_FILE = "../gcp-credential/key.json"

if __name__ == "__main__":

    folders = "./"
    audio_files = rec.get_audio_files_in_folder(folders)

    for f in audio_files:
        new_audio_path = rec.check_and_convert_audio(f)

        # To use GCP Speech API with long audio file(>1min),
        # it should be located in the Google Cloud Storage.
        gsutil_url = bucket.upload_to_gcs(source_file_path=new_audio_path,
                                          bucket_name=BUCKET_NAME, 
                                          destination_blob_name=os.path.split(new_audio_path)[1], 
                                          credentials_file=CREDENTIALS_FILE)