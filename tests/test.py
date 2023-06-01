import pytest
from flask import Flask
from app.main import search, format_results

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_search_with_name(client):
    response = client.get('/search?name=Lee')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Lee Whitebrook'

def test_search_with_city(client):
    response = client.get('/search?city=Byerazino')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['city'] == 'Byerazino'

def test_search_with_quantity(client):
    response = client.get('/search?quantity=3')
    assert response.status_code == 200
    assert len(response.json) == 3

def test_search_with_name_and_city(client):
    response = client.get('/search?name=Albertine&city=PÃ©rigueux')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'Albertine Mapson'
    assert response.json[0]['city'] == 'PÃ©rigueux'

def test_search_with_invalid_csv_path(client, monkeypatch, capsys):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr('builtins.open', mock_open)

    response = client.get('/search?name=John')
    assert response.status_code == 200
    assert response.json == []
    assert 'File not found.' in capsys.readouterr().out

def test_format_results():
    results = [
        {
            'id': '950',
            'name': 'Lee Whitebrook',
            'email': 'lwhitebrookqd@angelfire.com',
            'gender': 'Male',
            'company': 'Flashspan',
            'city': 'Byerazino'
        },
        {
            'id': '951',
            'name': 'Mic Dalgety',
            'email': 'mdalgetyqe@marriott.com',
            'gender': 'Genderqueer',
            'company': 'Photobean',
            'city': 'Massy'
        },
        {
            'id': '1000',
            'name': 'Dania Wyburn',
            'email': 'dwyburnrr@hp.com',
            'gender': 'Genderqueer',
            'company': 'Photofeed',
            'city': 'Dongdajie'
        }
    ]

    formatted_results = format_results(results)

    assert formatted_results[0]['id'] == '950'
    assert formatted_results[0]['name'] == 'Lee Whitebrook'
    assert formatted_results[0]['email'] == 'lwhitebrookqd@angelfire.com'
    assert formatted_results[0]['gender'] == 'Male'
    assert formatted_results[0]['company'] == 'Flashspan'
    assert formatted_results[0]['city'] == 'Byerazino'
    assert formatted_results[50]['id'] == '1000'
    assert formatted_results[50]['name'] == 'Dania Wyburn'
    assert formatted_results[50]['email'] == 'dwyburnrr@hp.com'
    assert formatted_results[50]['gender'] == 'Genderqueer'
    assert formatted_results[50]['company'] == 'Photofeed'
    assert formatted_results[50]['city'] == 'Dongdajie'