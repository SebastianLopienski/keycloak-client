[![Documentation Status](https://readthedocs.org/projects/keycloak-client/badge/?version=latest)](https://keycloak-client.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/akhilputhiry/keycloak-client.svg?branch=master)](https://travis-ci.com/akhilputhiry/keycloak-client)
![CI](https://github.com/akhilputhiry/keycloak-client/workflows/CI/badge.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/keycloak.svg)](https://badge.fury.io/py/keycloak)
[![codecov](https://codecov.io/gh/akhilputhiry/keycloak-client/branch/master/graph/badge.svg)](https://codecov.io/gh/akhilputhiry/keycloak-client)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c0d666b018207a00d27/maintainability)](https://codeclimate.com/github/akhilputhiry/keycloak-client/maintainability)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/keycloak.svg)](https://pypistats.org/packages/keycloak)

This repo contains a python client for [Keycloak](https://www.keycloak.org/).
Documentation is available in [https://keycloak-client.readthedocs.io](https://keycloak-client.readthedocs.io)


### Installation

```
pip install keycloak              # install only client   
pip install keycloak[docs]        # install client + sphinx   
pip install keycloak[extensions]  # install client + django/flask/starlette   
pip install keycloak[complete]    # insgall client + sphinx + django/flask/starlette   
```

### Web Framework Support

We provide prebuilt middlewares for the following frameworks

* Flask
* Starlette
* Django


### Usage / Examples

```
>>>
>>> from keycloak import Client
>>>
>>>
>>> kc = Client()  # for realm client
>>> kc = Client(username="akhilputhiry", password="*****")  # for realm users
>>>
>>>
>>> kc.userinfo
{'sub': 'e1fbd7d6-ad2b-407f-89cf-6c2b004d78bb', 'email_verified': False, 'preferred_username': 'service-account-python-client', 'email': 'service-account-python-client@placeholder.org'}
>>>
>>>
>>> kc.resources
['bb6a777f-a17b-4555-b035-a6ce12a1fd21']
>>>
>>>
>>> kc.find_resource('bb6a777f-a17b-4555-b035-a6ce12a1fd21')
{'name': 'Default Resource', 'type': 'urn:python-client:resources:default', 'owner': {'id': 'd74cc555-d46c-4ef8-8a30-ceb2b91d8823'}, 'ownerManagedAccess': False, 'attributes': {}, '_id': 'bb6a777f-a17b-4555-b035-a6ce12a1fd21', 'uris': ['/*'], 'resource_scopes': []}
>>>
>>>
>>> kc.access_token
'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJHYkdydV9sa05wN29hdjg1MUx4LXRQT1c3LWdCeWRKRWZIYmUxRHp1Zm1NIn0.eyJqdGkiOiI3YTFiMzEzZS0xMWMyLTRlY2EtODE2Ny1lYWZkNGJhZDRiZGUiLCJleHAiOjE1NzIyMDA1NjMsIm5iZiI6MCwiaWF0IjoxNTcyMjAwNTAzLCJpc3MiOiJodHRwczovL2tleWNsb2FrLmFraGlscHV0aGlyeS5kZXYvYXV0aC9yZWFsbXMvbWFzdGVyIiwiYXVkIjpbInB5dGhvbi1jbGllbnQiLCJhY2NvdW50Il0sInN1YiI6ImUxZmJkN2Q2LWFkMmItNDA3Zi04OWNmLTZjMmIwMDRkNzhiYiIsInR5cCI6IkJlYXJlciIsImF6cCI6InB5dGhvbi1jbGllbnQiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiIyMDYxZDMxZC02OTYwLTQxNTEtYjA0ZC03MDEzYmIwZTgzY2IiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJweXRob24tY2xpZW50Ijp7InJvbGVzIjpbInVtYV9wcm90ZWN0aW9uIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJjbGllbnRIb3N0IjoiMTgwLjE1MS4xMzcuMTQwIiwiY2xpZW50SWQiOiJweXRob24tY2xpZW50IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzZXJ2aWNlLWFjY291bnQtcHl0aG9uLWNsaWVudCIsImNsaWVudEFkZHJlc3MiOiIxODAuMTUxLjEzNy4xNDAiLCJlbWFpbCI6InNlcnZpY2UtYWNjb3VudC1weXRob24tY2xpZW50QHBsYWNlaG9sZGVyLm9yZyJ9.f6_s1UvWiQEiAsA6nIlsEbMuFOslPdhXbDKiGzWMfZGqYsgP5YvSoY3x6eqLRV-9hKZUcN0ksORkrPwl1Rtln9yK_jH0xBCzYhoKHeM3mffvYsypL9p3ZKLuH0Z3SqvHEQMtXbPlQ-yQUzFNtUw5AxljSOZNlbB6gTaJLX0-u6a4dMwGUpJ_QRVEQdtyt7R4RkI7Lxp2z3o8InILTt6Pxq6Hpx9bqIy7z8OTkZobpZuk9NAsKYoC5DhdlXOB9GQyr4h7Xc09p6fi5Lbq2W8ixL_6M-uJUvNo5s_XNCUjrFD6vnGBDTcozQxTETfGx7tvYx3ru4k3i9b2EnZ08olvVw'
>>>
>>>kc.refresh_token
'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyZTliNDk1Ny04ZGY0LTQwZjMtYjI0NS04ZjYxNmNlNGNiYmMifQ.eyJqdGkiOiI0NjcwYzhlMy1kZTgxLTQ2MzMtOWNjZi1jZmJkNDA3YzY0OGQiLCJleHAiOjE1ODQwODUwOTEsIm5iZiI6MCwiaWF0IjoxNTg0MDgzMjkxLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvYXV0aC9yZWFsbXMvbWFzdGVyIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL21hc3RlciIsInN1YiI6ImUwNDk0ZDEyLTg4NjktNDIyMi04MGFkLTU1ZTM0NjljMmEyZSIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJrZXljbG9hay1jbGllbnQiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiJhOTJhZGI1ZS1lMWFlLTQzNjgtOGVhMC02NDY4NGFmOTdmOWUiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImtleWNsb2FrLWNsaWVudCI6eyJyb2xlcyI6WyJ1bWFfcHJvdGVjdGlvbiJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIn0.NDjtHxP-ACt2sj349hHx1v5MK1z8PP_b-z_74M7mvxc'
>>>
>>>
```
