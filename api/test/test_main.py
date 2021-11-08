import requests
from .helper import relative_url

def test_get_titles():
    response = requests.get(relative_url("/api/titles"))
    assert response.status_code == 200
