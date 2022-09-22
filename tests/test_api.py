"""
    Integrations tests for Golden Raspberry Awards API.

    All the redundant client.get is intentional
    to test multiple calls in a row.
"""

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_get_intervals_must_be_200_status(client):
    response = client.get("/intervals")
    assert response.status_code == status.HTTP_200_OK


def test_get_intervals_must_return_valid_json(client):
    response = client.get("/intervals")
    assert response.headers["Content-Type"] == "application/json"


def test_get_intervals_must_return_dict(client):
    response = client.get("/intervals")
    assert isinstance(response.json(), dict)


def test_get_intervals_must_return_min_list(client):
    response = client.get("/intervals")
    assert isinstance(response.json()["min"], list)


def test_get_intervals_min_list_must_not_be_empty(client):
    response = client.get("/intervals")
    assert len(response.json()["min"]) > 0


def test_get_intervals_min_list_must_contain_all_fields(client):
    response = client.get("/intervals").json()["min"][0]
    assert "producer" in response
    assert "interval" in response
    assert "previousWin" in response
    assert "followingWin" in response


def test_get_intervals_min_list_fields_must_be_correct_types(client):
    response = client.get("/intervals").json()["min"][0]
    assert isinstance(response["producer"], str)
    assert isinstance(response["interval"], int)
    assert isinstance(response["previousWin"], int)
    assert isinstance(response["followingWin"], int)


def test_get_intervals_must_return_max_list(client):
    response = client.get("/intervals")
    assert isinstance(response.json()["max"], list)


def test_get_intervals_max_list_must_not_be_empty(client):
    response = client.get("/intervals")
    assert len(response.json()["max"]) > 0


def test_get_intervals_max_list_must_contain_all_fields(client):
    response = client.get("/intervals").json()["max"][0]
    assert "producer" in response
    assert "interval" in response
    assert "previousWin" in response
    assert "followingWin" in response


def test_get_intervals_max_list_fields_must_be_correct_types(client):
    response = client.get("/intervals").json()["max"][0]
    assert isinstance(response["producer"], str)
    assert isinstance(response["interval"], int)
    assert isinstance(response["previousWin"], int)
    assert isinstance(response["followingWin"], int)
