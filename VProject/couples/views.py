#-*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer

from serializers import CoupleSerializer


class CoupleListView(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    model = User
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = CoupleSerializer
    renderer_classes = (UnicodeJSONRenderer, )

    def list(self, request, *args, **kwargs):
        return super(CoupleListView, self).list(self, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = CoupleSerializer(data=request.DATA)
        if serializer.is_valid():
            print 'hello'
            User.objects._create_user(
                couple_name=serializer.data['couple_name'],
                man=serializer.data['man'],
                woman=serializer.data['woman'],
                d_day=serializer.data['d_day'],
            )
            print 'hello2'
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print serializer._errors

            if 'couple_name' in serializer._errors:
                couple_name_error = serializer._errors.get('username', None)
                if couple_name_error == serializer._errors.get('username', None):
                    return Response(serializer._errors, status=status.HTTP_409_CONFLICT)
            else:
                return Response(serializer._errors, status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        print 'get_queryset'
        couple = self.request._user
        print "couple.id : %s" % couple.id
        return User.objects.filter(id=couple.id)

    def destroy(self, request, *args, **kwargs):
        return super(CoupleListView, self).destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CoupleListView, self).update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CoupleListView, self).retrieve(request, *args, **kwargs)