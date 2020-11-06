"""Module service."""
import requests


class ModuleClass1:

    def add_two_number(self, n1, n2) -> int:
        return n1 + n2

    def multiply_two_number(self, n1, n2) -> int:
        return n1 * n2


class ModuleClass2:

    def get_my_ip(self) -> str:
        """Get ip."""
        response = requests.get('http://ipinfo.io/json')
        return response.json()['ip']
