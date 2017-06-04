from nose.tools import *

from tests import test_app

def test_dashboard_server_is_up_and_running():
    response = test_app.get("/")
    assert response.status_code == 200
