from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from RestApi.service import service


def getOrganizationList(request):
    organization = service.getOrganizationList()
    return JsonResponse({'organization': organization}, safe=False)


def getDiaryInOutYearAgainstOrganization(request, organizationId, startDate, endDate):
    years = service.getDiaryInOutYearAgainstOrganization(organizationId, startDate, endDate)
    return JsonResponse({'organizationInOutListCount': years}, safe=False)


def getMonthDiaryInOutBasedOnYear(request, organizationId, year):
    years = service.getMonthDiaryInOutBasedOnYear(organizationId, year)
    return JsonResponse({'organizationInOutMonthData': years}, safe=False)


def getMonthDiaryInOutBasedOnMOnth(request, organizationId,year,month):
    years = service.getMonthDiaryInOutBasedOnMonth(organizationId,year,month)
    return JsonResponse({'organizationInOutDayData': years}, safe=False)
