from nose.tools import *
import dashboard.index as dashboard

_globals = { "dashboard": None }

def setup_dashboard():
    _globals["dashboard"] = dashboard.app.test_client()

def teardown_dashboard():
    _globals["dashboard"] = None

@with_setup(setup_dashboard, teardown_dashboard)
def test_dashboard_server_is_up_and_running():
    response = _globals["dashboard"].get("/")
    assert response.status_code == 200
