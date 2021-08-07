from django.db import models
from django.contrib.auth.models import User


class Config(models.Model):
    name_project = models.CharField(max_length=80)
    key = models.CharField(max_length=80)
    token = models.CharField(max_length=80)
    todo_id = models.CharField(max_length=80)
    in_progress_id = models.CharField(max_length=80)
    code_review_id = models.CharField(max_length=80)
    in_test_id = models.CharField(max_length=80)
    release_id = models.CharField(max_length=80)
    done_id = models.CharField(max_length=80)
    board_id = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name_project