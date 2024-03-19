import data_extract as de
import push_to_GCSBucket as pGCS

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/allrounders'
headers = {
	"X-RapidAPI-Key": "443409f4c6msh6286dfce62077e0p1ad446jsn97e9eb4f1f69",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}
querystring = {"formatType":"odi"}
csv_filename = 'odi_allrounder_rankings1.csv'
projectId="cricket-rankings-analytics"

de.extract_to_csv(url, headers, querystring, csv_filename)
pGCS.upload_to_gcs(csv_filename, project_id=projectId)