from django.db import models
# // we need 2-3 to generate random code
import string
import random

# //generates random code for the room//
def generate_unique_code():
    length = 6 

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code 


# Create your models here.
class Room(models.Model):
    # //code for the room//
    code = models.CharField(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, unique=True)
    # //sets the rule for the guests
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    # //when the room is created, automatically add the date and time it was created at//
    created_at = models.DateTimeField(auto_now_add=True)

    