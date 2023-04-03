from django.shortcuts import render

# Create your views here.
from snippets.models import Snippet
from snippets.models import Goods
from snippets.serializers import SnippetSerializer
from snippets.serializers import GoodsSerializer
from snippets.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SnippetList(APIView):

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    列出所有的snippets或者创建一个新的snippet。
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    检索，更新或删除一个snippet示例。
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUserInfo(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` 实例。
            'auth': str(request.auth),  # None
        }
        return Response(content)


class GoodsList(APIView):

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    列出所有的snippets或者创建一个新的snippet。
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    """
    检索，更新或删除一个snippet示例。
    """
    def get_object(self, pk):
        try:
            return Goods.objects.get(pk=pk)
        except Goods.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        goods = self.get_object(pk)
        serializer = GoodsSerializer(goods)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        goods = self.get_object(pk)
        serializer = GoodsSerializer(goods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        goods = self.get_object(pk)
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
