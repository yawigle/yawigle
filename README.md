# yawigle
Yet Another Wigle.net API client (WIP).

Check https://api.wigle.net/swagger for the API documentation.

## Installation

```bash
python3 -m pip install yawigle
```

## API Key

Go to https://wigle.net/account and click on `Show my token`

## Examples

### Get SSID, Latitude and Longitude of a Wifi MAC Address
```python
In [1]: from yawigle import client
In [2]: c = client('AIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
In [3]: nets = c.network.detail('fa:8f:ca:71:92:09')
In [4]: f"{nets[0]['ssid']} is located at {nets[0]['trilat']} {nets[0]['trilong']}"
Out[4]: 'Kitchen speaker.o is located at 37.23993301 -115.79644012'
```

### Search network by SSID
```python
In [1]: from yawigle import client                                        
In [2]: c = client('AIDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx','xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
In [5]: nets = c.network.search(ssid='McDonalds Free WiFi')               
In [6]: nets[0]                 
Out[6]: 
{'trilat': 29.92946053,
 'trilong': -95.95930481,
 'ssid': 'McDonalds Free WiFi',
 'qos': 5,
 'transid': '20140703-00000',
 'firsttime': '2014-07-02T14:00:00.000Z',
 'lasttime': '2015-09-14T16:00:00.000Z',
 'lastupdt': '2015-09-14T16:00:00.000Z',
 'netid': '00:00:00:00:04:26',
 'name': None,
 'type': '????',
 'comment': None,
 'wep': '?',
 'bcninterval': 0,
 'freenet': '?',
 'dhcp': '?',
 'paynet': '?',
 'userfound': False,
 'channel': 0,
 'encryption': 'unknown',
 'country': 'US',
 'region': 'TX',
 'housenumber': None,
 'road': 'FM 362',
 'postalcode': '77484',
 'city': 'Waller'}
```

