import requests
from .helper import relative_url

def test_get_titles():
    response = requests.get(relative_url("/api/titles"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 100

    for i in range(100):
        assert response_body[i]["id"] == f'{i}'
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] in ["Freehold", "Leasehold"]
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]

def test_get_titles_by_class():
    response = requests.get(relative_url("/api/titles?title_class=freehold"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 100

    for i in range(100):
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] == "Freehold"
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]
