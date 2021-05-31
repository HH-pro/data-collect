from django.db import models



class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=50)
    econtact = models.CharField(max_length=30)


class Meta:
    ordering = ['-created_on']


# this method is the default human-readable representation of the object. Django will use it in many places
# such as the admin panel
def __str__(self):
    return self.title
