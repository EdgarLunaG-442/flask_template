from models import BlackList
from api import create_app
from faker import Faker
import unittest
import os
from copy import deepcopy
from flask_jwt_extended import decode_token
from models import db, BlackList


class TestBlackList(unittest.TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.tokens = []
        self.fkr = Faker()

    def setUp(self) -> None:
        self.app_uuid = os.getenv("API_UUID")
        self.tkn = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBfdXVpZCI6Ijg0ZTUzMmNiLT" \
                   "A3ODgtNDcyOS1hMzc5LTFmNjY3ZjE4YTQ0MyJ9.wTHH_sbnfimd3b-BvJ-AfKWU7YdH9QWSesDcTQDzqgQ"
        self.app = create_app('config.default', test_mode=True)

    '''Endpoint health check.'''

    def test_health_check(self):
        response = self.app.get('/health')
        response_code = response.status_code
        self.assertEqual(200, response_code)

    '''Add email to blacklist'''

    def test_add_email_to_blackist(self):
        mock_email = self.fkr.email()
        payload = {
            "email": mock_email,
            "app_uuid": f"{self.app_uuid}",
            "blocked_reason": f"{self.fkr.paragraph(nb_sentences=2)}",
        }
        response = self.app.post(f'/blacklist', headers={'Authorization': f'Bearer {self.tkn}'}, json=payload)
        response_code = response.status_code
        response_json: dict = response.get_json()
        self.assertEqual(200, response_code)
        self.assertEqual(f"El correo {mock_email} fue añadido a la lista negra exitosamente", response_json.get("msg", None))

    '''verify if email is inside blacklist'''

    def test_email_in_blackist(self):
        def filter_object(elem, fields):
            copy_elem = deepcopy(elem)
            for field in fields:
                copy_elem.pop(field)
            return copy_elem

        blacklist_email_dict = {
            "email": self.fkr.email(),
            "app_uuid": f"{self.app_uuid}",
            "blocked_reason": f"{self.fkr.paragraph(nb_sentences=2)}",
            "ip": f"{self.fkr.ipv4()}"
        }
        filtered_blacklist_email_dict = filter_object(blacklist_email_dict, ["app_uuid"])
        blacklist_email = BlackList(**filtered_blacklist_email_dict)
        blacklist_email.add()
        payload = filter_object(blacklist_email_dict, ["ip"])
        response = self.app.get(f'/blacklist/{blacklist_email.email}', headers={'Authorization': f'Bearer {self.tkn}'})
        response_code = response.status_code
        response_json: dict = response.get_json()
        saved_email = BlackList.query.filter_by(email=blacklist_email_dict["email"]).all()
        self.assertEqual(200, response_code)
        self.assertEqual(True, response_json.get("in_list", None))
        self.assertEqual(saved_email[0].email,blacklist_email_dict["email"])


    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
