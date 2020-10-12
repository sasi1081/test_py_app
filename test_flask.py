from app import home
import requests
def test_home():
    assert home() == "<h1>Hello , Greetings from Sasi!</p>"
    
def test_version():
    response = requests.get("http://localhost:5000/version")
    assert response.headers["Content-Type"] =="application/json"

def test_version_message():
    response = requests.get("http://localhost:5000/version")
    response_body = response.json()
    assert response_body["Description"] == "Practice Test"
