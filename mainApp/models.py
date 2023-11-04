from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='place', blank=True, null=True)
    price = models.FloatField()
    day = models.PositiveSmallIntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Travel(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    persons = models.PositiveSmallIntegerField()
    about = models.TextField()

    def __str__(self):
        return f"{self.place}: {self.persons} person"


class Action(models.Model):
    image = models.ImageField(upload_to='action', blank=True, null=True)
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.title}'


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='employee', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.position}"


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"


class Comment(models.Model):
    full_name = models.CharField(max_length=255)
    comment = models.TextField()
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"
