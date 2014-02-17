# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import viewsets, mixins, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer

from serializers import UserSerializer, UserCreateSerializer


class UserListCreateView(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    renderer_classes = (UnicodeJSONRenderer, )

    def list(self, request, *args, **kwargs):
        return super(UserListCreateView, self).list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        계정을 생성
        """
        serializer = UserCreateSerializer(data=request.DATA)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.data['username'],
                password=serializer.data['password'],
                email=serializer.data['email'],
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer._errors

            if 'username' in serializer._errors:
                username_error = serializer._errors.get('username', None)
                if username_error == [u'User with this Username already exist.']:
                    return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):
    model = User
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer, )

    def get_queryset(self):
        print 'get_queryset'
        user = self.request.user
        print "user.id : %s" % user.id
        return User.objects.filter(id=user.id)

    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)


class TokensViewSet(viewsets.GenericViewSet,
                    mixins.CreateModelMixin):
    """
    아이디와 패스워드를 이용하여
    API 사용을 위한 인증 토큰을 생성한다.

    """
    permission_classes = (AllowAny,)
    renderer_classes = (UnicodeJSONRenderer, )
    serializer_class = AuthTokenSerializer
    model = Token

    def initial(self, request, *args, **kwargs):
        super(TokensViewSet, self).initial(request, *args, **kwargs)

        if isinstance(request.DATA, dict):
            for key in request.DATA.keys():
                if type(request.DATA[key]) is list:
                    request.DATA[key] = request.DATA[key][0]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.object['user'])
            id_num = serializer.object['user'].id
            return Response({'token': token.key, 'id': id_num})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
