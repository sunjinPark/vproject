from rest_framework import serializers
from models import Couples


class CoupleSerializer(serializers.HyperlinkedModelSerializer):
    #get, update, delete post list
    class Meta:
        model = Couples
        fields = ('couple_name', 'man', 'woman', 'd_day')

