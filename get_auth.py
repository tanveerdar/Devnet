import requests as requests
from requests.auth import HTTPBasicAuth

DNAC_USER = "devnetuser"
DNAC_PASSWORD = "Cisco123!"


def get_auth_token():
    url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"  # Endpoint URL
    resp = requests.post(
        url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD)
    )  # Make the POST Request
    token = resp.json()["Token"]  # Retrieve the Token from the returned JSON
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token


if __name__ == "__main__":
    get_auth_token()
