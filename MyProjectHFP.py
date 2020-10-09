import urllib3, requests, json

# retrieve your iam_service_credentials_username, iam_service_credentials_password, and iam_service_credentials_url from the
# Service credentials associated with your IBM Cloud.

iam_credentials={
"url": iam_service_credentials_url,
"username": iam_service_credentials_username,
"password": iam_service_credentials_password
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=iam_credentials['username'], password=iam_credentials['password']))
url = '{}/identity/token'.format(iam_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5faa4d90-8469-4e8d-a443-a97dbc3da9a4/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))
