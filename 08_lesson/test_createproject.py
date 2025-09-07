import requests
import pytest

url = "https://ru.yougile.com"

# Позитивные проверки


@pytest.mark.parametrize(
    "token",
    [""],
)
def test_create_project_positive(token: str):
    url = "https://ru.yougile.com"
    new_project = {"title": "Python"}
    headers = {
        "Authorization": f"Bearer {token}"
    }
    resp = requests.post(url+'/api-v2/projects', json=new_project,
                         headers=headers)
    assert resp.status_code == 201
    response = resp.json()
    id = response["id"]
    assert id

# Негативные проверки


@pytest.mark.parametrize(
    "token",
    [""],
)
def test_create_project_negative(token: str):
    new_project = {"title": ""}
    headers = {
        "Authorization": f"Bearer {token}"
    }
    resp = requests.post(url+'/api-v2/projects',
                         json=new_project, headers=headers)
    assert resp.status_code == 400
    text = "title should not be empty"
    assert text

# Изменение проекта. Позитивные проверки


@pytest.mark.parametrize(
    "token",
    [""],
)
def test_change_positive(token: str):
    project = {"deleted": False,
               "title": "TIMESQUARE8"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
        }
    split = '/api-v2/projects/4ab29094-a00b-4309-b875-b1fe286ec9ae'
    resp = requests.request("PUT", url+split, json=project, headers=headers)
    print(resp.text)
    expected_code = 200
    assert resp.status_code == expected_code
    response = resp.json()
    assert response

# Негативные проверки


@pytest.mark.parametrize(
    "token",
    [""],
)
def test_change_negative(token: str):
    project = {"id": "4ab29094-a00b-4309-b875-b1fe286ec9ae"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
        }
    resp = requests.put(url+'/api-v2/projects/', json=project, headers=headers)
    assert resp.status_code == 404
    text = "Not Found"
    assert text

# Получение проекта. Позитивные проверки


@pytest.mark.parametrize(
    "token",
    [""],
)
def test_get_positive(token: str):
    project = {"id": "4ab29094-a00b-4309-b875-b1fe286ec9ae"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
        }
    split = '/api-v2/projects/4ab29094-a00b-4309-b875-b1fe286ec9ae'
    resp = requests.get(url+split, json=project, headers=headers)
    assert resp.status_code == 200
    responce = resp.json()
    assert responce
    text = "title: Питон1"
    assert text

# Негативные проверки(Неверный токен)


@pytest.mark.parametrize("token", [""])
def test_get_negative(token: str):
    project = {"id": "4ab29094-a00b-4309-b875-b1fe286ec9ae"}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
        }
    split = '/api-v2/projects/4ab29094-a00b-4309-b875-b1fe286ec9ae'
    resp = requests.get(url+split, json=project, headers=headers)
    assert resp.status_code == 401
    responce = resp.json()
    assert responce
    text = "message: Unauthorized"
    assert text
