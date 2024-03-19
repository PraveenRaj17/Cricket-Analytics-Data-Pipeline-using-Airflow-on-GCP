from google.cloud import storage

csv_filename = "odi_allrounder_rankings.csv"

project_id="cricket-rankings-analytics"

def upload_to_gcs(csv_filename, project_id, bucket_name='bkt_ar_ranking_data'):
    # Create a storage client and get the bucket
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)

    # Set the destination blob name
    destination_blob_name = csv_filename

    # Upload the file to GCS
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(csv_filename)

    # Print upload confirmation
    print(f"File {csv_filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

if __name__ == "__main__":
    upload_to_gcs(csv_filename, project_id, bucket_name='bkt_ar_ranking_data')