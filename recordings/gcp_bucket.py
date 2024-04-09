from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name, credentials_file):
    # Initialize the Google Cloud Storage client with the credentials
    storage_client = storage.Client.from_service_account_json(credentials_file)

    # Get the target bucket
    bucket = storage_client.bucket(bucket_name)

    # Upload the file to the bucket
    print(f"Initialize Blob storage instance..")
    blob = bucket.blob(destination_blob_name)
    print(f"Upload file into the Blob")
    blob.upload_from_filename(source_file_path)

    gsutil_url = f"gs://{bucket_name}/{destination_blob_name}"
    print(f"File {source_file_path} uploaded to {gsutil_url}")

    return gsutil_url