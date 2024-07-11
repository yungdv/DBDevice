from django.db import models

class EquipmentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hardware(models.Model):
    sn = models.CharField(max_length=50)
    inventn = models.CharField(max_length=50)
    created = models.DateField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sn} ({self.model.name})"
