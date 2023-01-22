from django.db import models
from django.utils.translation import gettext as _

class Score(models.Model):
    
    name = models.CharField(_("Name"), max_length=300)
    points = models.PositiveIntegerField(_("Points"))

    def __str__(self):
        return self.name 