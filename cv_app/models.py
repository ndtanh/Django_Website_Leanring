from django.db import models


# Create your models here.
class BaseInformation(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True, unique=True)
    gender_choice = (
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other")
    )
    gender = models.CharField(max_length=7, choices=gender_choice)
    apply_to = models.CharField(max_length=100, blank=False)
    career_objectives = models.TextField(blank=True)
    about = models.TextField(blank=True)
    list_display = ('full_name', 'email')

    def __str__(self):
        return self.full_name


class Education(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    GPD = models.FloatField(default=0)

    def __str__(self):
        return self.school


class Activity(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateField()
    place = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    mission = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.DateField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    time_start = models.DateField()
    time_end = models.DateField()
    skill = models.CharField(max_length=400)
    content = models.CharField(max_length=200)
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    user = models.ForeignKey(BaseInformation, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    time_start = models.DateField()
    time_end = models.DateField()
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.company_name
