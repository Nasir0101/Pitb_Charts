from django.urls import path
from . import views

urlpatterns = [
    path('organizations/', views.getOrganizationList),
    path('dairy/inout/<int:organizationId>/<str:startDate>/<str:endDate>', views.getDiaryInOutYearAgainstOrganization),
    path('dairy/months/inout/<int:organizationId>/<str:year>', views.getMonthDiaryInOutBasedOnYear),
    path('dairy/dates/inout/<int:organizationId>/<str:year>/<str:month>', views.getMonthDiaryInOutBasedOnMOnth)
]
