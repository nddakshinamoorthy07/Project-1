from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email


class StaffAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitchen_id = models.IntegerField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    skill = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.name} - Kitchen {self.kitchen_id}"


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.name} - {self.date} - {self.status}"
