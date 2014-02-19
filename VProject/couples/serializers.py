from rest_framework import serializers
from models import Couples


class CoupleSerializer(serializers.HyperlinkedModelSerializer):
  #  man = serializers.RelatedField(many=True)
 #   woman = serializers.RelatedField(many=True)

    #get, update, delete post, list
    class Meta:
        model = Couples
        fields = ('couple_name', 'man', 'woman', 'd_day',)


