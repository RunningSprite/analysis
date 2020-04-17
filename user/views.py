from django.http import JsonResponse
from rest_framework import status
from .models import User
from rest_framework.decorators import api_view
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.renderers import  JSONRenderer  #导入序列化数据转json数据的模块

# 实例化该类
jr = JSONRenderer()
@api_view(['GET', 'POST'])
def user_list(request):
    # 访问方式
    # http://127.0.0.1:8000/api/user_list/
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        print('请求成功')
        return Response(serializer.data)

    # 添加一个对象
    elif request.method == 'POST':
        # serializer = UserSerializer(data=request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print('serializer校验通过')
            serializer.save()
            print('serializer存储成功')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# def user(request, pk, format=None):
def user(request):
    # 加了 id 后的访问方式
    # http://127.0.0.1:8000/api/user/1/
    try:
        # get 方式需要验证，而 filter 方式不用验证
        # user = User.objects.get(id=pk)
        print(request.GET.get('id'))
        user = User.objects.filter(id=request.GET.get('id'))
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    # put 方式用不了
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        print('测试serializer')
        print(serializer)
        if serializer.is_valid():
            print('进入测试serializer')
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if(user.delete()):
            print('删除成功')
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def delete_user(request):
    try:
        # get 方式需要验证，而 filter 方式不用验证
        # user = User.objects.get(id=pk)
        print(request.GET.get('id'))
        # user = User.objects.filter(id=request.GET.get('id'))
        user = User.objects.get(id=request.GET.get('id'))
        print(user)
        user.delete()
        print('删除成功')
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # id == request.GET.get('id')
    # print('删除成功')
    # # user = User.objects.filter('id')
    # user.delete()
    # print('删除成功')
    # return Response(status=status.HTTP_204_NO_CONTENT)
