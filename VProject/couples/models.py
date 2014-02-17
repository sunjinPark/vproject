# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Couples(models.Model):
    man = models.ForeignKey(User)
    woman = models.ForeignKey(User)
    couple_name = models.CharField(primary_key=True, max_length=50, null=False, help_text='커플 닉네임', unique=True)
    d_day = models.DateField()