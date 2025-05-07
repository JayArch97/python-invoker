import urllib.request
import urllib.parse
import json
import google.oauth2.id_token


def make_authorized_get_request(endpoint, audience):

    data = urllib.parse.urlencode({'key': 'This is mock data that will be sent'})
    data = data.encode('ascii')

    # uses the urlib library to get the endpoint
    req = urllib.request.Request(endpoint, data=data)



    # uses the authentication library to get the credintials. 
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)
    print(response.read())
    return response.read()


#testing the function with the endpoint and audiance.
make_authorized_get_request('https://python-target-974768286444.us-central1.run.app/hello' , 'https://python-target-974768286444.us-central1.run.app')