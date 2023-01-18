from django.db import models
from django.utils.translation import gettext as _

class Question(models.Model):

    LEVELS = (
        (0, _("Any")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert"))
    )

    title = models.CharField(_("Title"), max_length=300)
    points = models.PositiveSmallIntegerField(_("Points"))
    difficulty = models.IntegerField(_("Difficulty"), choices=LEVELS, default=0)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):

    question = models.ForeignKey(to=Question, related_name='answer', verbose_name=_("Question"), on_delete=models.CASCADE)
    answer = models.CharField(_("Answer"), max_length=300)
    is_correct =models.BooleanField(_("Correct Answer"), default=False)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    def __str__(self):
        return self.answer