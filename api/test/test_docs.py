import requests
from .helper import relative_url

def test_get_docs():
    response = requests.get(relative_url("/docs"))
    assert response.status_code == 200
