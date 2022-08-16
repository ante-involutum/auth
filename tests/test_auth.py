from email import header
import pytest


@pytest.mark.usefixtures('init')
class TestAuth():

    payload = {
        'name': "admin",
        'password': "admin"
    }

    header = {
        "Authorization": "admin"
    }

    def test_auth(self):
        resp = self.bs.post('/auth/password/', json=self.payload)
        assert resp.status_code == 200

    def test_pass(self):

        resp = self.bs.get('/auth/authorization/', headers=self.header)
        assert resp.status_code == 200
