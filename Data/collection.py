from functions import *
from configs import *

#Inputs for the request
bearer_token = bearer_token
headers = create_headers(bearer_token)
# keyword = "machine learning lang:en"
keyword = "machine learning"
start_time = "2022-01-31T00:00:00.000Z"
end_time = "2022-02-03T00:00:00.000Z"
max_results = 10


url = create_url(keyword, start_time,end_time, max_results)

json_response = connect_to_endpoint(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))

# print(json_response['data'][0]['created_at'])