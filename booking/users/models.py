from django.db import models
from django.forms import ModelForm

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=20)
    birthdate = models.DateField('Birthdate')
    def __unicode__(self):
        return ("%s,%s,%s,%s,%s") %(self.firstname, self.lastname, self.username, self.password, self.email)
    
class UserForm(ModelForm):
    class Meta:
	model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password', 'birthdate']
        
        