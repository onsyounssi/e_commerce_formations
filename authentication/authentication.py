from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from datetime import datetime, timedelta 

User = get_user_model

class JWTAuthentication(authentication.BaseAuthentication):
    # create auth
    def authenticate(self, request):
        # Extract token from http header
        jwt_token = self.get_the_token_from_header(request.META.get('HTTP_AUTHORIZATION'))
        if not jwt_token:
            return None
        
        
        try: 
            # decode the jwt token with the secret key
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithme=['HS256'],
                                 audience=settings.JWT_CONF['JWT_AUDIENCE']) 
        except jwt.ExpiredSignatureError:
            return AuthenticationFailed('token has expired')
        except jwt.InvalidTokenError as err:
            raise AuthenticationFailed(f" Invalid token !: {str(err)}")
        user_id= payload.get('user_identifier')
        if user_id is None:
            raise AuthenticationFailed('user identifier not found in JWT')
        user= User.objects.filter(id=user_id)
        if user is None:
            raise AuthenticationFailed('user not found')
        return user, payload
        
    def authorization_header(self, request):
        return 'Bearer'
    
    @staticmethod
    def get_the_token_from_header(authorization_header): 
        # remove 'Bearer' if   exist and clean up spaces
        if authorization_header and authorization_header.lower().startswith('bearer'):
            return authorization_header.split('',1)[1].strip()
        return None 
    
    # creation json web token  
    @staticmethod
    def create_jwt(user):
        # Generate jwt token with extended expiration and user info 
        payload = {
            "user_identifier": user.id,
            "exp" :int((datetime.now() + timedelta(hours=settings.JWT_CONF ['TOKEN_LIFETIME_HOURS'])).timestamp),
            "iat" : datetime.now().timestamp(), # db
            "email": user.email,
            "is_active": user.is_active  
        }
        
        payload ['aud'] = settings.JWT_CONF.get("JWT_AUDIENCE",'my_app') 
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return jwt_token