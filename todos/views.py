from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .serializers import TodoSerializer, TodoDtoSerializer
from .models import Todo

from core.models import AmqpMessage, FastPublisher

import os

# Create your views here.
publisher = FastPublisher(name=os.getenv('TODOS_EXCHANGE'))

@api_view(['GET'])
@permission_classes([AllowAny])
@swagger_auto_schema(tags=['todos'], responses={200: TodoSerializer})
def get_todos(request):
    todos = Todo.objects.all()
    if not todos:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = TodoDtoSerializer(todos, many=True)
    publisher.publish(message=AmqpMessage(
        routing_key=os.getenv('TODOS_ALL_ROUTING_KEY'),
        body=serializer.data
    ))

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
@swagger_auto_schema(tags=['todos'], responses={200: TodoSerializer})
def get_todo(request, id):
    todo = Todo.objects.filter(id=id).first()
    if not todo:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoDtoSerializer(todo)

    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method="POST", tags=["todos"], request_body=TodoSerializer
)
@api_view(["POST"])
@permission_classes([AllowAny])
def post_todo(request):
    serializer = TodoSerializer(data=request.data)
    serializer.validate(attrs=request.data)

    if serializer.is_valid():
        todo = serializer.save()
        serializer = TodoDtoSerializer(todo)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method="PUT", tags=["todos"], request_body=TodoSerializer
)
@api_view(["PUT"])
@permission_classes([AllowAny])
def put_todo(request, id):
    todo = Todo.objects.filter(id=id).first()
    if not todo:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo, data=request.data)
    serializer.validate(attrs=request.data)

    if serializer.is_valid():
        todo = serializer.save()
        serializer = TodoDtoSerializer(todo)

        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method="DELETE", tags=["todos"])
@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_todo(request, id):
    todo = Todo.objects.filter(id=id).first()
    if not todo:
        return Response(status=status.HTTP_404_NOT_FOUND)

    todo.delete()

    return Response(
        {
            "deletedId": id
        },
        status=status.HTTP_200_OK,
    )