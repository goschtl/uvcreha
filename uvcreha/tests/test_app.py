import morepath
import uvcreha

from webtest import TestApp as Client


def test_root():
    morepath.scan(uvcreha)
    morepath.commit(uvcreha.App)

    client = Client(uvcreha.App())
    root = client.get('/')

    assert root.status_code == 200
    assert '/greeting/world' in root
    assert '/greeting/mundo' in root
