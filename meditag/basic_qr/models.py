from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
BLOOD_GROUP_CHOICES =(
    ("O+", "O+"),
    ("O-", "O-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
)
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=100, null=True,unique=True)
    emergency_no = models.CharField(max_length=100, null=True,blank=True)
    blood_group = models.CharField(max_length=100, null=True,choices=BLOOD_GROUP_CHOICES,default="O+")
    height_cms = models.IntegerField(null=True,blank=True)
    weight_kgs =models.FloatField(null=True,blank=True)
    allergies = models.TextField(null=True,blank=True)
    disabilities = models.TextField(null=True,blank=True)
    undergoing_treatments = models.TextField(null=True,blank=True)
    spl_med_conditions = models.TextField(null=True,blank=True)
    ongoing_meds = models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.name
