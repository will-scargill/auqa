import unittest
import index

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = index.app.test_client()

    def test_server_is_up_and_running(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
