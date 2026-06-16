import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app.test_client()
    with app.app_context():
        db.drop_all()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_socketio_connect():
    # Basic smoke test
    assert True  # Expand later with SocketIO test client
