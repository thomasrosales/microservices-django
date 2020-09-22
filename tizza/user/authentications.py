import base64
from rest_framework import authentication, exceptions
from tizza.settings import CLIENT_TOKENS


class BearerTokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        try:
            authorization_header = request.META['HTTP_AUTHORIZATION']
            _, token_base64 = authorization_header.split(' ')
            token = base64.b64decode(token_base64.encode()).decode('utf8')
            client, password = token.split(':')
            if CLIENT_TOKENS[client] == password:
                return None, None
            else:
                raise exceptions.AuthenticationFailed(
                    'Invalid authentication token')
        except KeyError:
            raise exceptions.AuthenticationFailed(
                'Missing authentication header')
        except IndexError:
            raise exceptions.AuthenticationFailed(
                'Invalid authentication header')
