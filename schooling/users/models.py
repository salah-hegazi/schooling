from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class School(models.Model):
    """
    A model that represents a school entity
    """
    code = models.CharField(_("Code of school"), max_length=10, unique=True)
    name = models.CharField(_("Name of school"), max_length=100)
    address = models.CharField(_("Address of school"), max_length=150)

    def __str__(self):
        return self.name


class Grade(models.Model):
    """
    A model that represents school years
    """
    code = models.CharField(_("Code of grade"), max_length=10, unique=True)
    name = models.CharField(_("Name of grade"), max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='grades')

    def __str__(self):
        return self.name


class User(AbstractUser):
    """
    A model that represents all system users
    """
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


class Parent(models.Model):
    """
    A profile model that stores more information related to user type parent
    """
    # Using phonenumber_field third package to
    # define phone number in E.164 format
    phone_number = PhoneNumberField(_("Phone number of Parent"), unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='parent')
    schools = models.ManyToManyField(School, related_name='parents')

    def __str__(self):
        return self.user.username


class ManagerialEmployee(models.Model):
    """
    A profile model that stores more information related to user type staff
    """
    # Using phonenumber_field third package to
    # define phone number in E.164 format
    phone_number = PhoneNumberField(_("Phone number of Employee"),
                                    unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='staff')
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='staff')

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    """
    A profile model that stores more information related to user type Teacher
    """
    # Using phonenumber_field third package to
    # define phone number in E.164 format
    phone_number = PhoneNumberField(_("Phone number of Teacher"), unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='teacher')
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='teachers')

    def __str__(self):
        return self.user.username


class ClassRoom(models.Model):
    """
    A model that represents school's classrooms
    """
    code = models.CharField(_("Code of classroom"), max_length=10,
                            unique=True)
    name = models.CharField(_("Name of classroom"), max_length=50,
                            unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name='classrooms')
    location = models.CharField(_("Location of classroom"), max_length=50,
                                blank=True)
    teachers = models.ManyToManyField(Teacher, related_name='classrooms')

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    A profile model that stores more information related to user type student
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='student')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,
                               related_name='students')
    school = models.ForeignKey(School, on_delete=models.CASCADE,
                               related_name='students')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                  related_name='students')
    teachers = models.ManyToManyField(Teacher, related_name='students')

    def __str__(self):
        return self.user.username

