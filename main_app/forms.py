from user.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'country']