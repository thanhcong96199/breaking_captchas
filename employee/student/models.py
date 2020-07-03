from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


def gen_unique_code():
    return uuid.uuid4().hex[:16].upper()


class Student(AbstractUser):
    email = models.EmailField(blank=True, null=True, max_length=254, unique=True)
    username = models.CharField(blank=True, null=True, max_length=254, unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this student belongs to. A student will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="student_set",
        related_query_name="student",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('student_set permissions'),
        blank=True,
        help_text=_('Specific permissions for this student_set.'),
        related_name="student_set",
        related_query_name="student_set",
    )

    class Meta:
        db_table = 'tbl_student'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email


class LoadAndGenImage:
    url = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'tbl_load_gen_image'