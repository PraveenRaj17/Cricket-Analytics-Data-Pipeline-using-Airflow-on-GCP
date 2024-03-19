from google.cloud import storage

local_file_path = '/Users/praveenrajveluswami/Documents/DataEngineeringProjects/Cricket-Analytics-Data-Pipeline-using-Airflow-on-GCP/odi_allrounder_rankings.csv'  # Replace with the path to your local file
bucket_name = 'bkt_ar_ranking_data'  # Replace with your GCS bucket name
destination_blob_name = 'odi_ar_rankings.csv'  # Replace with the name you want to give the file in GCS
project_id = "cricket-rankings-analytics"

def upload_to_gcs(local_file_path, bucket_name, destination_blob_name, project_id):
    # Create a storage client and get the bucket
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)

    # Upload the file to GCS
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)

    print(f"File {local_file_path} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

def fgrg():
    print("jkbdfkjds")