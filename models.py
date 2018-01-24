from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Dimitri DUBOIS'

doc = """
The final screen. It displays the final payoff and an area from the subject 
to write comments about the experiment"
"""


class Constants(BaseConstants):
    name_in_url = 'final_screen'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comments = models.LongStringField(blank=True)
