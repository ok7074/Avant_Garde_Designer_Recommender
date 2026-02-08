import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("pinterest_api_key")

def make_api_call(url="https://de.pinterest.com/homefeed//v1/pinterest/search", method="get", data=None, params=None, headers={ "x-api-key": f"Bearer {api_key}"}):

    # Set up the request method

    request_method = getattr(requests, method.lower())

    try:
        # Make the request
        response = request_method(
            url,
            json=data,
            params=params,
            headers=headers,
            timeout=10  # Add timeout to prevent hanging
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Return JSON response if applicable
        if 'application/json' in response.headers.get('content-type'):
            return response.json()
        return response.text

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
        # Get error details if available
        try:
            error_details = response.json()
            print(f"Error details: {error_details}")
        except:
            print(f"Response text: {response.text}")

    except requests.exceptions.ConnectionError:
        print("Connection Error: Failed to connect to the API")

    except requests.exceptions.Timeout:
        print("Timeout Error: The request timed out")

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")

    return None