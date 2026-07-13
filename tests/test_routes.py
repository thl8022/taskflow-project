import pytest

from app import app
from src.services import create_task, get_all_tasks


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_dashboard_page(client):
    response = client.get("/dashboard")

    assert response.status_code == 200


def test_new_task_page(client):
    response = client.get("/new")

    assert response.status_code == 200


def test_create_task(client):

    response = client.post(
        "/new",
        data={
            "title": "Teste Pytest",
            "description": "Descrição de teste",
            "priority": "Alta",
            "status": "Pendente"
        },
        follow_redirects=True
    )

    assert response.status_code == 200


def test_delete_task(client):

    create_task(
        "Excluir",
        "Teste",
        "Baixa",
        "Pendente"
    )

    task = get_all_tasks()[0]

    response = client.get(
        f"/delete/{task['id']}",
        follow_redirects=True
    )

    assert response.status_code == 200
