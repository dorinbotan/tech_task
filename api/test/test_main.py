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

def test_get_titles_with_limit():
    response = requests.get(relative_url("/api/titles?_limit=10"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 10

    for i in range(10):
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] in ["Freehold", "Leasehold"]
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]

def test_get_titles_with_pagination():
    response = requests.get(relative_url("/api/titles?_page=1&_limit=10"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 10

    for i in range(10):
        assert response_body[i]["id"] == f'{i+10}'
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] in ["Freehold", "Leasehold"]
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]

def test_get_titles_with_sort():
    response = requests.get(relative_url("/api/titles?_sort=title_class&_order=desc"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 100

    for i in range(100, 1):
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] == "Leasehold"
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]

def test_get_titles_with_order():
    response = requests.get(relative_url("/api/titles?_sort=id&_order=desc"))
    assert response.status_code == 200

    response_body = response.json()
    assert len(response_body) == 100

    for i in range(100, 1):
        assert response_body[i]["title_number"] is not None
        assert response_body[i]["title_class"] in ["Freehold", "Leasehold"]
        assert "_id" not in response_body[i]
        assert "content" not in response_body[i]

def test_get_single_title():
    response = requests.get(relative_url("/api/titles/101"))
    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == f'{101}'
    assert response_body["title_number"] is not None
    assert response_body["title_class"] in ["Freehold", "Leasehold"]
    assert "_id" not in response_body
    assert "content" is not None
