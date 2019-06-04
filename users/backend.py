from .models import MyUser

class EmailBackend(object):
    def authenticate(self,username=None, password=None):

        user = MyUser.objects.get(email=username)
        if user.check_password(password):
            return user


    def get_user(self, user_id):

        user= MyUser.objects.get(pk=user_id)
        if user.is_active:
            return user

