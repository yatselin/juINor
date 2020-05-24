from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count

from .models import Vacancy, Company, Specialty
from .forms import ApplicationForm

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
    form = ApplicationForm()
    context = {"vacancy": vacancy,
                "form": form}
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
    vacancies_all = get_list_or_404(Vacancy, specialty=specialty_obj)
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

def my_CV(request):
        context = {}
        return render(request, 'resume-edit.html', context)

def my_company(request):
        context = {}
        return render(request, 'company-edit.html', context)

def my_company_vacancies(request):
        context = {}
        return render(request, 'vacancy-list.html', context)

def my_company_vacancy(request, id):
        context = {}
        return render(request, 'vacancy-edit.html', context)

def vacancies_send(request, id):
        form = ApplicationForm(request.POST)
        vacancy = Vacancy.objects.get(pk=id)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.save()
            context = {"vacancy": vacancy}
            return render(request, 'sent.html', context)



def page_not_found(request, exception):
        return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
        return render(request, "misc/500.html", status=500)