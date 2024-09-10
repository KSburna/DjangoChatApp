from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    received = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']
        app_label = 'chat_app_pro'
        db_table = 'message'

    def __str__(self):
        return f'From {self.from_user.username} to {self.to_user.username}: {self.content[:20]}'
