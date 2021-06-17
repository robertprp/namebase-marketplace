"""
Includes Request class for convenience which applies consistent Timeout, Headers and Base URL settings.
"""
__all__ = ['get_current_time_milliseconds', 'Request']

import requests
import time
import json


def get_current_time_milliseconds():
    return round(time.time() * 1000)


class Request(object):
    def __init__(self, api_base_url, headers, cookies, timeout=30):
        self.url = api_base_url
        self.timeout = timeout
        self.headers = headers
        self.cookies = cookies

    def get(self, path, params=None):
        """GET request"""
        r = requests.get(url=self.url + path, params=params, timeout=self.timeout,
                         headers=self.headers, cookies=self.cookies)
        r.raise_for_status()
        return r.json()

    def post(self, path, data=None, json_data=None, params=None):
        """POST request"""
        url = self.url + path
        print(data)
        r = requests.post(url=url, data=json.dumps(data), json=json_data, params=json.dumps(params), timeout=self.timeout,
                          headers=self.headers, cookies=self.cookies)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return json.loads(e.response.content)
        return r.json()

    def put(self, path, data=None, json_data=None, params=None):
        """PUT request"""
        url = self.url + path
        r = requests.put(url=url, data=data, json=json_data, params=params, timeout=self.timeout,
                         headers=self.headers, cookies=self.cookies)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return json.loads(e.response.content)
        return r.json()

    def post_get_response(self, path, data=None, json_data=None, params=None):
        url = self.url + path
        r = requests.post(url=url, data=data, json=json_data, params=params, timeout=self.timeout,
                          headers=self.headers, cookies=self.cookies)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return json.loads(e.response.content)
        return r
