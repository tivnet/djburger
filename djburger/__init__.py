# -*- coding: utf-8 -*-
# built-in
from functools import partial       # noQA

# django
from django import forms            # noQA

# project
from . import controllers
from . import serializers
from . import validators

from .views import Rule, rule, ViewBase    # noQA


# shortcuts
f = forms
c = controllers
s = serializers
v = validators
