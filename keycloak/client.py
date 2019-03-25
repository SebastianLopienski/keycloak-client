#! -*- coding: utf-8 -*-
import os
import json

from .authentication import AuthenticationMixin
from .authorization import AuthorizationMixin
from .resource import ResourceMixin


class KeycloakClient(AuthenticationMixin, AuthorizationMixin, ResourceMixin):

    def __init__(self, config_file=None):
        """
        Method to initialize keycloak client

        Args:
            config_file(str): path to the keycloak config file
        """

        # default config file to keycloak.json
        config_file = 'keycloak.json' if config_file is None else config_file

        # validate config file
        if not os.path.isfile(config_file):
            raise ValueError('Unable to find the config file in the given path')

        # read config file
        with open(config_file, 'r') as file_descriptor:
            file_content = file_descriptor.read()

        # validate file is json loadable
        try:
            config = json.loads(file_content)
        except json.decoder.JSONDecodeError:
            raise ValueError('Invalid json file')

        # validate whether the required configs are present or not
        assert 'client_id' in config
        assert 'client_secret' in config
        assert 'redirect_uri' in config
        assert 'authentication_endpoint' in config
        assert 'token_endpoint' in config
        assert 'introspection_endpoint' in config

        # load config to object
        self.config = config