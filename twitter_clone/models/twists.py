from django.db import models
from django.contrib.auth.models import User

class Twist(models.Model):
    user = models.ForeignKey(
        User, related_name="meeps",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f" ({self.created_at:%d/%m/%Y %H:%M}): "
            f"{self.body}..."
        )