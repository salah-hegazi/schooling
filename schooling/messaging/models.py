from django.db import models
from django.conf import settings


class Message(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='received_mgs',
                                related_query_name='received_messages')
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='sent_mgs',
                                  related_query_name='sent_messages')
