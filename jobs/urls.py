from django.urls import path


from . import views

urlpatterns = [

    path(
        "vacancies/cat/<str:specialty>",
        views.spec_vacancies, name="spec_vacancies"),
    path("vacancies/<int:vacancy_id>", views.vacancy, name="vacancy"),
    path("vacancies/", views.vacancies, name="vacancies"),
    path(
        "companies/<int:company_id>",
        views.company_profile, name="company_profile"),
    path("companies/", views.companies, name="companies"),
    path("my_company/", views.my_company, name="my_company"),
    path("my_CV/", views.my_CV, name="my_CV"),
    path("", views.index, name="index"),
]
