import pytest
from fai import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['TESTING'] = True
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
