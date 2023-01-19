from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return "%s , %s , %s" % (self.key, self.user, self.created)
