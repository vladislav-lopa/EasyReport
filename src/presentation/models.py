from django.db import models
from report.models import Config


class PresentationData(models.Model):
    presentation_name = models.CharField(max_length=3600, null=True, )
    unfinished = models.CharField(max_length=3600)
    task_in_release = models.CharField(max_length=3600)
    completed = models.CharField(max_length=3600)
    story_points = models.CharField(max_length=3600)
    board_name = models.CharField(max_length=80)
    presentation = models.ForeignKey(Config, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.presentation_name
