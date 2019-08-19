from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


"""
class FixedFieldsModel(models.Model):

    # An abstract model that have common fields among multiple models.
    # Models that have these fields will inherit from this model.
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True    
"""


class User(AbstractUser):
    TYPE_CHOICES = [
        ('P', 'Parent'),
        ('M', 'Managerial Employee'),
        ('T', 'Teacher'),
        ('S', 'Student'),
    ]

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    type = models.CharField(_("Type of User"), max_length=1,
                            choices=TYPE_CHOICES)
    address = models.TextField(_("Address of User"), blank=True,
                               max_length=140)
    bio = models.TextField(_("Bio of User"), blank=True,
                           default=_('Hi there I am here'), max_length=140)
    picture = models.ImageField(_("Image of User"), upload_to='images/',
                                default='images/default.png')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
