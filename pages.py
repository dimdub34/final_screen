from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Final(Page):
    form_model = "player"
    form_fields = ["comments"]
    pass


class Final_after_comments(Page):
    pass


page_sequence = [Final, Final_after_comments]
