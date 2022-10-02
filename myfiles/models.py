from django.db import models

# Create your models here.
class murojaat(models.Model):
    ism = models.CharField(max_length=30)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
    murojat= models.TextField()
    vaqt = models.DateTimeField(auto_now=True)



class Mobiles(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    rasm5 = models.ImageField(upload_to='media')
    rasm6 = models.ImageField(upload_to='media')
    rasm7 = models.ImageField(upload_to='media')
    rasm8 = models.ImageField(upload_to='media')
    malumot = models.TextField()
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Audioss(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    rasm5 = models.ImageField(upload_to='media')
    rasm6 = models.ImageField(upload_to='media')
    rasm7 = models.ImageField(upload_to='media')
    rasm8 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Computers(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Household(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Kitchen(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Newproducts(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)



class Headphone(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)
class mr3(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)


class Laptop(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Desktop(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Wearable(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Tv(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Camera(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)

class Grinder(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)


class Tegishli(models.Model):
    model = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media')
    rasm3 = models.ImageField(upload_to='media')
    rasm4 = models.ImageField(upload_to='media')
    narxi = models.CharField(max_length=30)
    chegirma = models.CharField(max_length=30)
    vaqt = models.DateTimeField(auto_now=True)