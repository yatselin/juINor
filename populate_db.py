import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'junior.settings')

import django
django.setup()

import data
from jobs.models import Specialty, Company, Vacancy


def add_speciality(code, title):
    spec = Specialty.objects.create(code=code, title=title)
    spec.save()
    return spec


def add_company(name):
    company = Company.objects.create(name=name)
    company.save()
    return company


def add_vacancy(title, speciality, company, salary_min, salary_max,
                published_at, description):
    vacancy = Vacancy.objects.create(
                                    title=title,
                                    specialty=speciality,
                                    company=company,
                                    salary_min=salary_min,
                                    salary_max=salary_max,
                                    published_at=published_at,
                                    description=description)
    vacancy.save()
    return vacancy


def populate_db():
    print("-- adding specialities")
    for spec in data.specialties:
        add_speciality(spec['code'], spec['title'])

    print("-- adding companies")
    for company in data.companies:
        add_company(company['title'])

    print("-- adding jobs")
    for job in data.jobs:
        cat = Specialty.objects.get_or_create(title=job['cat'])[0]
        company = Company.objects.get_or_create(name=job['company'])[0]
        add_vacancy(job['title'], cat, company, job['salary_from'],
                    job['salary_to'], job['posted'], job['desc'])


if __name__ == '__main__':
    print('Starting populating script from data.py...')
    populate_db()
    print("Database was populated")
