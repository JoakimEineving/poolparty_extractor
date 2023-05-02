import requests

# Replace these with your poolparty credentials
username = '<USERNAME>'
password = '<PASSWORD>'

# Replace with your organization poolparty url
url = '<your organization poolparty url>/extractor/api/annotate'
# Replace with your input RDF file path
input_rdf_file = '<FILE NAME> ex input.rdf'
document_uri = 'https://example.com/uri'
project_id = '<PROJECT ID>'

# Read the contents of the input RDF file
with open(input_rdf_file, 'r', encoding='utf-8') as f:
    rdf_content = f.read()

payload = {
    'text': rdf_content,
    'documentUri': document_uri,
    'projectId': project_id
}

response = requests.post(url, data=payload, auth=(username, password))

if response.status_code == 200:
    print("Success! API response saved to 'output.rdf'")
    with open('output.rdf', 'w', encoding='utf-8') as f:
        f.write(response.text)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
