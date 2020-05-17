from django.db import models

class Specialty(models.Model):
    code = models.CharField(max_length=32)    
    title = models.CharField(max_length=32)
    picture = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.code

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='')
    logo = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    employee_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField()

    def __str__(self):
        return self.title    
