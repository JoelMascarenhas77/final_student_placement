from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self,username ,email ,key,password=None ):
        user = self.model(username=username,email=email)
        user.set_password(password)
        user.save(using=self._db)
        user.email=email
        user.info  = key
        return user

    def create_superuser(self, username,email, password=None):
      
        user = self.model(username=username,email=email)
        user.set_password(password)
        user.is_admin = True
        user.email=email
        user.save(using=self._db)
        return user
    


