# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class BankingConfig(AppConfig):
    name = 'banking'

    def ready(self):
    	import users.signals