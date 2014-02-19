# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Couples(models.Model):
    man = models.ForeignKey(User, related_name='+', unique=True)
    woman = models.ForeignKey(User, related_name='+', unique=True)
    couple_name = models.CharField(primary_key=True, max_length=50, null=False, help_text='커플 닉네임', unique=True)
    d_day = models.DateField()
"""
* 현재 상황 요약 *
PostMan에
couple_name : asdf
man : /user/1
woman : /user/2
d_day : 2011-02-06

으로 http://localhost:8000/couples에 Post날리면 500 오류가 뜸.
(간단한 거지만 man, woman에 url주소를 Post해야한다 것을 알아내기까지 오래걸렸던 것 같네요..
현재 아무렇게나 다른 영어를 POST하면 Invalid Hyper Link - NO URL이라고 오류메시지가 뜨고
/user/10 , /user/100 처럼 존재하지 않는 ID를 Post하면 object doesn' exsit라는 오류메시지가
뜨는 상황이고, 수정하려고 계속 찾아보고 있습니다 ㅠㅠ)

* 수정한 코드 및 설명 *
- related_name = "+" :
related_name을 설정하지 않으면,
Accessor for field 'man' clashes with related field 'User.couples_set'. Add a related_name argument to the definition for 'man'.
라고 오류가 뜸. Stackover Flow와 다큐먼트를 찾아 본 결과,
Foreign Key를 사용할 때, abstract models을 만들거나 special syntax를 이용하려면
사용해야 된다고함. backwards relation이 필요하지 않으면 그 값을 '+'로 하라고 하길래, +로 값을 지정.


- unique = True


"""

"""
    class Meta:
        unique_together = ('man', 'woman')

    def __unicode__(self):
        print self.man, self.woman
        return '%d: %s' % (self.man, self.woman)
"""