from django.views.decorators.http import require_http_methods
from rest_framework.response import Response 
# from django.http import JsonResponse 
from rest_framework import status
from .models import Category, SubCategory 
from .serializers import CategorySerializer, SubCategorySerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from authentication.authentication import JWTAuthentication 
from rest_framework.permissions import AllowAny, IsAuthenticated

################# CRUD: Category ####################

@api_view(['GET'])
@require_http_methods(['GET'])
@authentication_classes([JWTAuthentication]) #  @csrf acceder l'apis
@permission_classes([IsAuthenticated])

def get_all_catergory(request):
    """ GET : get all categories"""
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 
    #return JsonResponse({"data":serializer.data})
    
@api_view(['POST'])
@require_http_methods(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_category(request):
    """POST: create a category """
    data = request.data 
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@require_http_methods(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_category_by_id(request, id):
    """GET: get category by id """
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['DELETE'])
@require_http_methods(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_category(request, category_id):
    """DELETE : delete a category by is id """
    try: 
        category= Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"error":"Category not found"}, status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response({"message": "category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_category(request,pk):
    try:
        categories = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response({"error": "category not found"}, status= status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(categories, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "category update successfully"}, status=status.HTTP_200_OK)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
################# SubCategory ########################

@api_view(['GET'])
@require_http_methods(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_all_subcategory(request):
    """GET: get all category"""
    SubCategories = SubCategory.objects.all()
    serializer = SubCategorySerializer(SubCategories, many=True)
    return Response(serializer.data)
        
@api_view(['GET'])
@require_http_methods(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_subcategory_by_id(request,id):
    """GET: get subcategory by id """
    try:
        sub_category= SubCategory.objects.get(id=id)
    except SubCategory.DoesNotExist:
        return Response({"error": "subcategory not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = SubCategorySerializer(sub_category) 
    return Response(serializer.data) 


@api_view(['POST'])
@require_http_methods(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_sub_category(request):
    """POST: add a new sub_category"""
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"subCategory added successfully"},status=status.HTTP_201_CREATED)
    return Response({"error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@require_http_methods(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_subcategory(request, id):
    """PUT : update a subcategory by his id """
    try: 
        sub_category = SubCategory.objects.get(id=id)
    except SubCategory.DoesNotExist:
        return Response({"error": "sub category not found"}, status= status.HTTP_404_NOT_FOUND)
    serializer = SubCategorySerializer(sub_category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Subcategory updated successuflly"}, status=status.HTTP_200_OK)
    return Response(serializer.errors)
    
    
@api_view(['DELETE'])
@require_http_methods(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])   
def delete_subcategory(request,id):
    """DELETE: delete sub category"""
    try:
        sub_category = SubCategory.objects.get(id=id)
    except SubCategory.DoesNotExist:
        return Response({"error":"Subcategory not found"}, status=status.HTTP_404_NOT_FOUND)
    sub_category.delete()
    return Response({"message": "sub category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@require_http_methods(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_subcategory_by_category(request):
    """get all sub category by category id """
    category_id = request.data.get('category_id')
    if not Category.objects.filter(id=category_id).exists():
        return Response({"error": "category not found"}, status=status.HTTP_404_NOT_FOUND)
    subcategories = SubCategory.objects.filter(category_id=category_id)
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)
    
    
    