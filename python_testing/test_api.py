import requests

def test_list_users_status_ok():
    r = requests.get("https://reqres.in/api/users?page=2")

    # Status code should be 200 (OK)
    assert r.status_code == 200

    # Response should contain 'data' key with users
    body = r.json()
    assert "data" in body
    assert len(body["data"]) > 0
