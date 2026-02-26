import requests
import time

def test_predict():
    url = "http://127.0.0.1:5005/predict"
    data = {
        "temp": "33.09",
        "gas": "1713",
        "moisture": "76.00"
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("SUCCESS! Prediction completed without errors.")
            if "Risk:" in response.text:
                print("Found 'Risk:' in the HTML response.")
        else:
            print(f"FAILED with status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_predict()
