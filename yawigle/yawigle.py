import requests
import json
from requests.auth import HTTPBasicAuth

class client():
    WIGLE_API_URL = 'https://api.wigle.net/api/v2'

    def __init__(self, api_name, api_token):
        self.requests_session = requests.session()
        self._basic_auth = HTTPBasicAuth(api_name, api_token)
        self._num_requests = 0

        self.network = Network(self,'/network')
        self.bluetooth = Bluetooth(self,'/bluetooth')
        self.cell = Cell(self,'/cell')
        self.file = File(self,'/file')
        self.stats = Stats(self,'/stats')
        self.group = Group(self,'/group')
        self.profile = Profile(self,'/profile')

    def _do_get(self, endpoint, params=None):
        end_url = self.WIGLE_API_URL + '/' + endpoint
        resp = self.requests_session.get(end_url, auth=self._basic_auth, params=params)
        self._num_requests += 1
        return resp

    def _do_get_json(self, endpoint, params=None):
        resp = self._do_get(endpoint,params)
        if resp.status_code != 200:
            return None

        return json.loads(resp.text)
        
    def _do_post(self,endpoint,params=None):
        end_url = self.WIGLE_API_URL + '/' + endpoint
        resp = self.requests_session.post(end_url, auth=self._basic_auth, params=params)
        self._num_requests += 1
        return resp

    def _do_paged_get(self, endpoint, params=dict(), limit=100):
        ret = []
        resultCount = 0

        while True:
            resp = self._do_get(endpoint,params=params)
            if resp.status_code != 200:
                break

            temp = json.loads(resp.text)
            resultCount = temp['totalResults']
            ret += temp['results']

            params['searchAfter'] = temp['searchAfter']

            if len(ret) >= limit:
                break

            if len(ret) >= resultCount:
                break

        return ret


class Endpoint():
    def __init__(self, http_client, endpoint):
        self._http_client = http_client
        self._endpoint = endpoint

    def search(self, limit=100, **kwargs):
        method_location = self._endpoint + '/search'
        items = self._http_client._do_paged_get(method_location, params=kwargs, limit=limit)
        return items

    def detail(self,netid):
        method_location = self._endpoint + '/detail'
        item = self._http_client._do_get_json(method_location,params={'netid':netid})
        return item.get('results')

class Network(Endpoint):
    def geocode(self):
        pass

    def comment(self):
        pass

class Bluetooth(Endpoint):        
    pass 

class Cell(Endpoint):        
    def mccMnc(self):
        pass

class File(Endpoint):
    def upload(self):
        pass

    def transactions(self):
        pass

    def kml(self):
        pass

class Stats(Endpoint):
    def countries(self):
        pass

    def general(self):
        pass

    def group(self):
        pass

    def regions(self):
        pass

    def site(self):
        pass

    def standings(self):
        pass

    def user(self):
        pass

class Group(Endpoint):
    def admin(self):
        pass 

    def groupMembers(self):
        pass

class Profile(Endpoint):
    def apiToken(self):
        pass

    def user(self):
        pass