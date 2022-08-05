import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "gK0SjrmFwB2Hc6iSeyXFh0-6hT3AJV9NTfzg56E_wKYk"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14","f15","f16","f17","f18","f19","f20","f21","f22","f23","f24","f25","f26"]], "values": [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ef796a23-5b51-482f-ad6f-0ff216f8c48c/predictions?version=2022-08-02', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions = response_scoring.json()

print("Scoring response")
predictions=response_scoring.json()
#print(predictions)
pred=predictions['predictions'][0]['values'][0][0]
if(pred == 0):
    #pred = "No failure expected within 30 days."
    print("No failure expected within 30 days.") 
else:
     #pred = "Maintenance Required!! Expected a failure within 30 days.
     print("Maintenance Required!! Expected a failure within 30 days.")