import csv
import requests

url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/allrounders'
headers = {
	"X-RapidAPI-Key": "443409f4c6msh6286dfce62077e0p1ad446jsn97e9eb4f1f69",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}
querystring = {"formatType":"odi"}
csv_filename = 'odi_allrounder_rankings2.csv'

def extract_to_csv(url, headers, querystring, csv_filename):
    try:
        
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        if response.status_code == 200:
            data = response.json().get('rank', [])  # Extracting the 'rank' data
            
            if data:
                field_names = ['id','rank', 'name', 'country', 'rating', 'trend']  # Specify required field names
                
                with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()
                    
                    for entry in data:
                        writer.writerow({field: entry.get(field) for field in field_names})
                        
                print(f"Data fetched successfully and written to '{csv_filename}'")
            else:
                print("No data available from the API.")
                
        else:
            print("Failed to fetch data:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)

if __name__ == "__main__":
    extract_to_csv(url, headers, querystring, csv_filename)
