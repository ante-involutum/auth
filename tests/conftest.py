import os
import pytest

from requests_toolbelt.sessions import BaseUrlSession


env = os.getenv('ENV')
envs = {
    'loc': 'http://127.0.0.1:8001'
}


@pytest.fixture()
def init(request):
    url = envs[env]
    bs = BaseUrlSession(base_url=url)
    request.cls.bs = bs
