from django.db import models


class Contact(models.Model):
    MODE_OF_CONTACT = [("email", "Email"), ("phone",  "Phone")]
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_no = models.IntegerField()
    mode_of_contact = models.CharField(max_length=10, choices=MODE_OF_CONTACT)
    message = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)


