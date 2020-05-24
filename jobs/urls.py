from django.urls import path


from . import views

urlpatterns = [

    path(
        "vacancies/cat/<str:specialty>",
        views.spec_vacancies, name="spec_vacancies"),
    path("vacancies/<int:vacancy_id>", views.vacancy, name="vacancy"),
    path("vacancies/", views.vacancies, name="vacancies"),
    path('vacancies/<int:id>/send', views.vacancies_send, name='vacancies_send',),
    path(
        "companies/<int:company_id>",
        views.company_profile, name="company_profile"),
    path("companies/", views.companies, name="companies"),
    path("mycompany/", views.my_company, name="my_company"),
    path("mycompany/vacancies/", views.my_company_vacancies, name="my_company_vacancies"),
    path('mycompany/vacancies/<int:id>', views.my_company_vacancy, name='my_company_vacancy'),
    path("my_CV/", views.my_CV, name="my_CV"),
    path("", views.index, name="index"),
]
