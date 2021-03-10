from RestApi.Dictionary import MonthDictionary
from RestApi.models import Tbldiarydispatchregister, Tblorganization
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime

class service():

    @classmethod
    def getOrganizationList(cls):
        organizationList = []
        queryset = Tblorganization.objects.values('organizationid', 'title').distinct()
        for organization in queryset:
            organizationList.append({
                'key': organization['organizationid'],
                'value': organization['title']
            })
        return organizationList

    @classmethod
    def getDiaryInOutYearAgainstOrganization(cls, organizationId,startDate,endDate):
        organizationInOutListCount = []
        difference_in_years = relativedelta(datetime.strptime(endDate,'%Y-%m-%d'), datetime.strptime(startDate,'%Y-%m-%d')).years
        queryset = Tbldiarydispatchregister.objects.filter(organizationid=organizationId, created__range=(startDate,endDate)).values()
        if list(queryset).__len__() != 0:
            dataFrame = pd.DataFrame.from_records(queryset)
            yearslist = list(dataFrame['registeryear'].unique())
            if(difference_in_years >1):
                for year in yearslist:
                    incomingCount = dataFrame.index[(dataFrame['registeryear'] == year) & (dataFrame['registermode'] == 'Incoming')].values.tolist().__len__()
                    outgoingCount = dataFrame.index[(dataFrame['registeryear'] == year) & (dataFrame['registermode'] == 'Outgoing')].values.tolist().__len__()
                    organizationInOutListCount.append({
                        'Label': year,
                        'Incomingcount': incomingCount,
                        'outgoingCount': outgoingCount,
                    })
                return organizationInOutListCount
            else:
                monthList = list(dataFrame['registermonth'].unique())
                monthList.sort(key=int)
                if(monthList.__len__() > 1):
                    for month in monthList:
                        incomingCount = dataFrame.index[(dataFrame['registermonth'] == month) & (dataFrame['registermode'] == 'Incoming')].values.tolist().__len__()
                        outgoingCount = dataFrame.index[(dataFrame['registermonth'] == month) & (dataFrame['registermode'] == 'Outgoing')].values.tolist().__len__()
                        organizationInOutListCount.append({
                            'Label': MonthDictionary.Month.names[month],
                            'Incomingcount': incomingCount,
                            'outgoingCount': outgoingCount,
                        })
                    return organizationInOutListCount
                else:
                    dateList = list(pd.to_datetime(dataFrame['created']).dt.strftime('%d-%m-%y').unique())
                    dateList = sorted(dateList)
                    for date in dateList:
                        incomingCount = dataFrame.index[(dataFrame['created'].dt.strftime('%d-%m-%y') == date) & (dataFrame['registermode'] == 'Incoming')].values.tolist().__len__()
                        outgoingCount = dataFrame.index[(dataFrame['created'].dt.strftime('%d-%m-%y') == date) & (dataFrame['registermode'] == 'Outgoing')].values.tolist().__len__()
                        organizationInOutListCount.append({
                            'Label': datetime.strptime(date, '%d-%m-%y').strftime('%d'),
                            'Incomingcount': incomingCount,
                            'outgoingCount': outgoingCount,
                        })
                    return organizationInOutListCount


        return None


    @classmethod
    def getMonthDiaryInOutBasedOnYear(cls,organizationId,year):
        organizationInOutMonthData = []
        queryset = Tbldiarydispatchregister.objects.filter(organizationid=organizationId, registeryear=year).values()
        if list(queryset).__len__() != 0:
            dataFrame = pd.DataFrame.from_records(queryset)
            monthList = list(dataFrame['registermonth'].unique())
            monthList.sort(key=int)
            for month in monthList:
                incomingCount = dataFrame.index[(dataFrame['registermonth'] == month) & (dataFrame['registermode'] == 'Incoming')].values.tolist().__len__()
                outgoingCount = dataFrame.index[(dataFrame['registermonth'] == month) & (dataFrame['registermode'] == 'Outgoing')].values.tolist().__len__()
                organizationInOutMonthData.append({
                    'Label': MonthDictionary.Month.names[month],
                    'Incomingcount': incomingCount,
                    'outgoingCount': outgoingCount,
                })
            return organizationInOutMonthData

        return None


    @classmethod
    def getMonthDiaryInOutBasedOnMonth(cls,organizationId,year,month):
        organizationInOutDayData = []
        monthInDigit = list(MonthDictionary.Month.names.keys())[list(MonthDictionary.Month.names.values()).index(month)]
        queryset = Tbldiarydispatchregister.objects.filter(organizationid=organizationId, registeryear=year,registermonth=monthInDigit).values()
        if list(queryset).__len__() != 0:
            dataFrame = pd.DataFrame.from_records(queryset)
            dateList = list(pd.to_datetime(dataFrame['created']).dt.strftime('%d-%m-%y').unique())
            dateList = sorted(dateList)
            for date in dateList:
                incomingCount = dataFrame.index[(dataFrame['created'].dt.strftime('%d-%m-%y') == date) & (dataFrame['registermode'] == 'Incoming')].values.tolist().__len__()
                outgoingCount = dataFrame.index[(dataFrame['created'].dt.strftime('%d-%m-%y') == date) & (dataFrame['registermode'] == 'Outgoing')].values.tolist().__len__()
                organizationInOutDayData.append({
                    'Label': datetime.strptime(date, '%d-%m-%y').strftime('%d'),
                    'Incomingcount': incomingCount,
                    'outgoingCount': outgoingCount,
                })
            return organizationInOutDayData

        return None




