from django.db import models
  
from django.contrib.auth.models import User


class Specialty(models.Model):
    code = models.CharField(max_length=32)    
    title = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='', default='')

    def __str__(self):
        return self.code


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='')
    logo = models.ImageField(upload_to='', default='', null=True)
    description = models.CharField(max_length=255, default='')
    employee_count = models.IntegerField(default=0)
    #owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    specialty = models.ForeignKey(
                                    Specialty,
                                    on_delete=models.CASCADE,
                                    related_name='vacancies')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='vacancies')
    skills = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField()

    def __str__(self):
        return self.title    


class Application(models.Model):

    name = models.CharField(max_length=155)
    phone = models.CharField(max_length=55)
    cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', default=None, null=True)

    def __str__(self):
        return f'User: {self.name} // Vacancy: {self.vacancy}'
        
