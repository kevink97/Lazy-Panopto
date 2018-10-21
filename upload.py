def upload_blob(bucket_name, source_file_name, destination_blob_name):
    from google.cloud import storage

    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

# To be changed / deleted (call from another file)
#upload_blob("panopto", "C:\\Users\\William\\Desktop\\example.png"
#, "example.png")
