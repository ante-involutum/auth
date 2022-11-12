import os
import pytest

from requests_toolbelt.sessions import BaseUrlSession


env = os.getenv('ENV')
envs = {
    'loc': 'http://127.0.0.1:8001',
    'dev': 'http://atop.test:31695',
    'test': 'http://tink.test:31695',
    'prd': 'http://tink.com:31695',
}


@pytest.fixture()
def init(request):
    url = envs[env]
    bs = BaseUrlSession(base_url=url)
    request.cls.bs = bs
