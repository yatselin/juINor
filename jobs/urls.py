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
    path("", views.index, name="index"),
]
