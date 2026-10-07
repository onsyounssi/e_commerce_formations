from django.core.cache import cache
from .authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout, get_user_model
from datetime import datetime, timedelta
from .serializers import ObtainTokenSerializer
from django.http import JsonResponse
from users.models import User
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json 


User = get_user_model()

@api_view(['POST'])
@require_http_methods(['POST'])
@permission_classes([AllowAny]) # ouver par tout quelque user is authentified 
def sign_in(request):
    """ Login """
    data= json.loads(request.body)
    serializer = ObtainTokenSerializer(data=data)
    if serializer.is_valid():
        user_qs = User.objects.filter(email = data['email'])
        user = user_qs.first()
        user_auth = authenticate(request, username = data['email'], password=data['password'])
        
        if user and user_auth and not user.is_verified:
            current_user ={
                "id": user.id,
                "username":user.first_name,
                "email": user.email,
                "is_verified": user.is_verified,
                "is_admin": user.is_admin
            }
            
            return  JsonResponse({
                "message ": "user is not verified ", "CurrentUser": current_user
            }, status= 400)
            
        if user_auth:
            login(request, user)
            # creat token 
            jwt_token = str(JWTAuthentication.create_jwt(user)) #  transfert format str
            
            # build current user information 
            current_user ={
                "id": user.pk,
                "username": user.first_name,
                "email": user.email,
                "is_verified": user.is_verified,
                "is_admin": user.is_admin
            }
            
            # cache the current user details
            cache.set('CurrentUser', current_user)
            
            # update last expiration time
            user.token_last_expired = datetime.now()+ timedelta(hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS'])
            user.save()
            
            return JsonResponse({
                "message": "login successfully ", "token": jwt_token, "CurrentUser": current_user
            },status=200)         
    return JsonResponse({ "error": serializer.errors}, status=400)

@api_view(['POST'])
@require_http_methods(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    try:
        logout(request)
        return JsonResponse({
            "message": 'logout successfully'
        }, status=200)
        
    except AttributeError:
        return JsonResponse({
            "error": "user not authenticeted"
        }, status=400)
        




# solution autre
# from django.core.cache import cache
# from .authentication import JWTAuthentication
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate, login, get_user_model
# from datetime import datetime, timedelta, timezone
# from .serializers import ObtainTokenSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings

# User = get_user_model()

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def sign_in(request):
#     """ Login """
#     # 1. Utiliser request.data fourni par DRF (plus besoin de json.loads ou @require_http_methods)
#     serializer = ObtainTokenSerializer(data=request.data)
    
#     if serializer.is_valid():
#         # Utiliser les données validées du serializer
#         email = serializer.validated_data.get('email')
#         password = serializer.validated_data.get('password')
        
#         # Authentification avec Django
#         user_auth = authenticate(request, username=email, password=password)
        
#         if not user_auth:
#             return Response(
#                 {"error": "Identifiants invalides (email ou mot de passe incorrect)"}, 
#                 status=status.HTTP_401_UNAUTHORIZED
#             )

#         # Structure des données utilisateur
#         current_user = {
#             "id": user_auth.id,
#             "username": user_auth.first_name,
#             "email": user_auth.email,
#             "is_verified": user_auth.is_verified,
#             "is_admin": user_auth.is_admin
#         }

#         # Vérification du statut de confirmation de compte
#         if not user_auth.is_verified:
#             return Response(
#                 {"message": "L'utilisateur n'est pas vérifié", "CurrentUser": current_user}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         # Connexion et génération du JWT
#         login(request, user_auth)
#         jwt_token = str(JWTAuthentication.create_jwt(user_auth))

#         # Mise en cache (Note : utiliser une clé unique par utilisateur si nécessaire)
#         cache.set(f'CurrentUser_{user_auth.id}', current_user)

#         # Mise à jour de l'expiration
#         user_auth.token_last_expired = datetime.now(timezone.utc) + timedelta(
#             hours=settings.JWT_CONF['TOKEN_LIFETIME_HOURS']
#         )
#         user_auth.save()

#         return Response({
#             "message": "Connexion réussie", 
#             "token": jwt_token, 
#             "CurrentUser": current_user
#         }, status=status.HTTP_200_OK)

#     # 2. Si les champs 'email' ou 'password' manquent ou sont invalides dans Postman
#     return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
