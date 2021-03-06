from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import *
from .serializers import *

@api_view(['POST'])
def insert(req):
    #put/post--->req.data

    if 'name' in req.data and 'address' in req.data and 'sex' in req.data and 'national_num' in req.data:
        print("asdasda")
        trainee = Trainee.objects.create(name=req.data['name'],address=req.data['address'],sex=req.data['sex'],national_num=req.data['national_num'])
        data = TraineeApi(trainee)
        return Response(data.data,status=HTTP_201_CREATED)
    else:
        return Response({'error':'invalid data'},status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def List(request):
    courses = Trainee.objects.all()
    data = TraineeApi(courses,many=True)
    return Response(data.data,status=HTTP_200_OK)


@api_view(['GET'])
def GETCOURSE(request,id):
    course = Trainee.objects.get(id=id)
    data = TraineeApi(course)
    return Response(data.data)


@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update(req):
    c=TraineeApi(req.data)
    if('id' in req.data):

        course = Trainee.objects.get(id=req.data['id'])

        if'name' in req.data or 'address' in req.data or 'sex' in req.data or 'national_num' in req.data:
            if 'name' in req.data:
                course.name = req.data['name']
                print(req.data['address'])
            if 'address' in req.data:
                print("sadasdas")
                course.address = req.data['address']
            if 'sex' in req.data:
                course.sex = req.data['sex']
            if 'national_num' in req.data:
                course.national_num = req.data['national_num']
            else:
                return Response({'error': 'no data for update'}, status=HTTP_406_NOT_ACCEPTABLE)
            course.save()
            data=TraineeApi(course)

        return Response(data.data, status=HTTP_201_CREATED)
    else:
        return Response({'error': 'invalid data'}, status=HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
# @permission_classes([permissions.IsAdminUser])
@authentication_classes([authentication.TokenAuthentication])
def delete(req,id):
    c = Trainee.objects.filter(id=id).delete()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    return Response({'message':'deleted'}, status=HTTP_200_OK)