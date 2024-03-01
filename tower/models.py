from django.db import models

# Create your models here.
class Tower(models.Model):
    tower_num = models.CharField(max_length=50)
    address_tower = models.CharField(max_length=255)
    floors_num = models.CharField(max_length=10)
    statues_tower = models.CharField(max_length=50)
    value_tower = models.CharField(max_length=50)
    picture_tower = models.ImageField(upload_to="tower_picture/",null=True,blank=True)
    notes = models.CharField(max_length=300)
    
    def __str__(self):
        return self.address_tower
    
class Apartments(models.Model):
    tower = models.ForeignKey(Tower,on_delete=models.CASCADE)
    apartment_num = models.CharField(max_length=50)
    floor=models.CharField(max_length=10)
    space=models.CharField(max_length=30)
    rooms_num=models.CharField(max_length=10)
    rooms_service_num=models.CharField(max_length=10)
    wc_num=models.CharField(max_length=10)
    statues_apartment=models.CharField(max_length=50)
    rent=models.CharField(max_length=10)
    duration=models.CharField(max_length=10)
    maintenance=models.CharField(max_length=10)
    picture=models.ImageField(upload_to="apartments_picture/",null=True,blank=True)
    notes=models.CharField(max_length=300)
    def __str__(self):
        return f'{self.tower.tower_num} - Apartments {self.apartment_num}'
    
class Tenants (models.Model):
    tower = models.ForeignKey(Tower, on_delete=models.CASCADE)
    apartments = models.ForeignKey(Apartments,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    id_person=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    picture =models.ImageField (upload_to="tenants_picture/",null=True,blank=True)
    notes=models.CharField(max_length=300)
    
class Employees (models.Model):
    tower = models.ForeignKey(Tower,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    id_person=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    picture=models.ImageField (upload_to="employees_picture/",null=True,blank=True)
    notes=models.CharField(max_length=300)


