from users.models import User
from rest_framework.response import Response
from users.serializers import SignUpSerializer ,UpdateUserSerializer
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from django.views.decorators.http import require_http_methods
from rest_framework import status
from authentication.authentication import JWTAuthentication
from django.core import serializers
import json


@api_view(['POST'])
@require_http_methods(['POST'])
@permission_classes([AllowAny]) # to use api with out token // quellque soit user en register un compte sans token spécifique 
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def add_user(request):
    """"POST: create a new user account"""
    data=request.data
    data['password'] = make_password(data['password'])
    sign_up_serializer = SignUpSerializer(data=data)
    if sign_up_serializer.is_valid():
        sign_up_serializer.save()
        return Response({"message":"account created successfully", "data":sign_up_serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"error":sign_up_serializer.errors},status=status.HTTP_400_BAD_REQUEST) 


# solution 1: methode par n'apport qu'elle modele (from django.core import serializers)

# @api_view(['GET'])
# @require_http_methods(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def get_users(request):
#     """GET: get all users """
#     users_list=[]
#     users =  User.objects.all()
#     users_json = serializers.serialize('json',users)
#     print({"users_json":users_json})
#     print({"type_users_json":type(users_json)})
#     res = json.loads(users_json)
#     for i in range(len(res)):
#         res[i].pop('model')
#         trust_id = res[i]['pk']
#         res[i].pop('pk')
#         res[i]['fields'].pop('password')
#         res[i]['fields']['id'] = trust_id
#         users_list.append(res[i]['fields'])
#     return Response({"users":users_list},status=status.HTTP_200_OK)


# la solution : get all_users par methode serializers
@api_view(['GET'])
@require_http_methods(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_users(request):
    """GET: get all users """
    users = User.objects.all()
    serializer = SignUpSerializer(users,many=True)
    return Response({"users":serializer.data},status=status.HTTP_200_OK)

@api_view(['DELETE'])
@require_http_methods(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_users(request,pk):
    """"DELETE: delete a users by his id """
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({"message":"user deleted successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_user(request,pk):
    """PUT: update a user by his pk(id)"""
    try:
        user= User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({"error":"user not found"}, status= status.HTTP_404_NOT_FOUND)
    serializer = UpdateUserSerializer(user,data=request.data,partial=True) # Paptiel de changemment de update en fields de  user (updateserializer )
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"user updated successfully ",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    


@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def disable_user(request, user_id):
    """"PUT:disable user (modify le continue dans un attribut ou ligne)"""
    try:
        user=User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "user not found"},status=status.HTTP_404_NOT_FOUND)
    user.is_active = False
    user.save()
    return Response({"message": "user updated successfully"},status=status.HTTP_200_OK)

@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def  toggle_user(request, user_id):
    """ PUT: switch active or inactive for a user """
    try:
        user= User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND)
    user.is_active = not user.is_active
    user.save()
    return Response({"message":"user updated successfully"},status=status.HTTP_200_OK)

    
@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request, user_id):
    """PUT: change le password for a user """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND)
    data=request.data
    if check_password(data['current_password'], user.password):
        if data['new_password'] == data['confirm_password']:
            user.password = make_password(data['new_password'])
            user.save()
            return Response({"message":"password updated successfully "},status=status.HTTP_200_OK)
        else:
            return Response({"error":"password not confirm"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error":"password not matched"},status=status.HTTP_400_BAD_REQUEST)
    
        
    
