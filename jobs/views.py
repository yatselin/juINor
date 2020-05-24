from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count

from .models import Vacancy, Company, Specialty


def index(request):

    specialties = Specialty.objects.values(
            'code', 'title', 'picture').annotate(
            count=Count('vacancies'))
    companies = Company.objects.values(
            'name',
            'location',
            'logo',
            'description',
            'employee_count', 'id', 'logo').annotate(
            count=Count('vacancies'))
    context = {
                "specialties": specialties,
                "companies": companies
    }
    return render(request, 'index.html', context)


def vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    context = {"vacancy": vacancy}
    return render(request, 'vacancy.html', context)


def vacancies(request):
    vacancies_all = Vacancy.objects.all()
    vacancies = Vacancy.objects.values(
            'title',
            'specialty',
            'company',
            'skills',
            'description',
            'salary_min',
            'salary_max',
            'published_at', 'id').annotate(
            count=Count('specialty'))  
    context = {
                "text": "all vacancies here soon",
                "vacancies_all": vacancies_all,
                "vacancies": vacancies,
                "specialty": "Все вакансии"

    }
    return render(request, 'vacancies.html', context)


def spec_vacancies(request, specialty):
    specialty_obj = get_object_or_404(Specialty, code=specialty) 
    vacancies_all = get_list_or_404(Vacancy)
    vacancies = Vacancy.objects.values(
            'title',
            'specialty',
            'company',
            'skills',
            'description',
            'salary_min',
            'salary_max',
            'published_at', 'id').annotate(
            count=Count('specialty')).filter(specialty=specialty_obj)
    companies = Company.objects.all()
    context = {

            "vacancies": vacancies,
            "vacancies_all": vacancies_all,
            "specialty": specialty,
            "companies": companies}
    return render(request, 'vacancies.html', context)


def company_profile(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    vacancies = Vacancy.objects.values(
            'title',
            'specialty',
            'company',
            'skills',
            'description',
            'salary_min',
            'salary_max',
            'published_at', 'id').annotate(
            count=Count('company')).filter(company=company)
    context = {
            "company": company,
            "vacancies": vacancies}
    return render(request, 'company.html', context)


def companies(request):
    companies = Company.objects.values(
            'name',
            'location',
            'logo',
            'description',
            'employee_count', 'id').annotate(
            count=Count('vacancies'))
    context = {
                "companies": companies
    }
    return render(request, 'companies.html', context)
