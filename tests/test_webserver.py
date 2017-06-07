from nose.tools import *

from tests import test_app

# Check the web server works
def test_dashboard_server_is_up_and_running():
    # Go to the homepage
    response = test_app.get("/")
    # If the status code is 200 (success) then the test works.
    assert response.status_code == 200
