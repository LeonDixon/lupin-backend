from django.db import models

class Users(models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=20)
  email = models.EmailField()
  hased_password = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Passwords(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
  website = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  encrypted_password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)