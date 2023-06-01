import pytest
from flask import Flask

from app import main

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(main.app)
    app.testing = True
    client = app.test_client()
    return client


def test_search_without_parameters(client):
    response = client.get('/search')
    assert response.status_code == 200
    data = response.get_json()

def test_search_with_name_parameter(client):
    response = client.get('/search?name=Kimberly')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['Name'] == 'Kimberly'


def test_search_with_city_parameter(client):
    response = client.get('/search?city=Å½ivinice')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['City'] == 'Å½ivinice'


def test_search_with_quantity_parameter(client):
    response = client.get('/search?quantity=5')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 5


def test_search_with_multiple_parameters(client):
    response = client.get('/search?name=Kimberly&city=Å½ivinice&quantity=1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['Name'] == 'Kimberly'
    assert data[0]['City'] == 'Å½ivinice'
