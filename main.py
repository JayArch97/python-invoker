import google.oauth2.id_token
import google.auth.transport.requests
import jwt  # Added import for jwt
import logging  # Added import for logging
import requests # Added import for requests


def call_predictions(arr_dict, api_host, model_endpoint):

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, api_host)


    # Decode the ID token
    decoded_token = jwt.decode(id_token, options={"verify_signature": False})


    # Print the decoded token
    logging.info(f'decoded_token: {decoded_token}')

    headers = {'Authorization': 'Bearer {}'.format(id_token)}


    response = requests.post(api_host + "/" + model_endpoint, json=arr_dict,
    headers=headers, verify=False)

    try:
        preds = response.json()
        print(f"Predictions: {preds}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON for predictions: {e}")
        preds = None



    return preds

call_predictions({'key1': 'value10', 'key2': 'value20'} , 'https://python-target-974768286444.us-central1.run.app', 'hello'  )