from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

POETS = [
    ("Machine", "Machine"),
    ("Shakespeare", "Shakespeare"),
    ("Ginsberg", "Ginsberg"),
    ("Cummings", "Cummings"),
    ("Lorem Ipsum", "Lorem Ipsum")
]


class Input(models.Model):
    style = models.CharField(choices=POETS, default=POETS[0], max_length=100)
    first_line = models.CharField(max_length=1000, null=True, blank=True)
    # TODO another input options
    keywords = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str: return self.style + " | " + self.first_line


class Poem(models.Model):
    author = models.CharField(choices=POETS, default=POETS[0], max_length=100)
    input = models.ForeignKey(Input, on_delete=models.DO_NOTHING, null=True, blank=True)
    text = models.CharField(max_length=100000, default="")
    views = models.IntegerField(default=0)
    sentiment = models.CharField(max_length=100, null=True, blank=True)
    generator_type = models.CharField(max_length=100, default="full")
    style_transfer = models.IntegerField(default=0)
    translations = models.CharField(max_length=100000, default="", blank=True)
    bleu_score = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('views',)
    
    def __str__(self) -> str:
        return str(self.id) + " | " + self.author


class Rate(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.DO_NOTHING)
    rate = models.IntegerField()
    category = models.CharField(default="overall", max_length=100)



class TuringTestVote(models.Model):
    VOTES = [
        ("Human", "Human"),
        ("Machine", "Machine")
    ]

    poem = models.ForeignKey(Poem, on_delete=models.DO_NOTHING)
    fragment = models.CharField(max_length=200, null=True, blank=True)
    vote = models.CharField(choices=VOTES, default="Machine", max_length=100)

