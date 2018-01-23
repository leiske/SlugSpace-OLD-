# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 02:45:52 2018 
Created for Cruz Hacks 2018
This script will handle partitioning to create a predictive algorithm. 

@author: Raul B. Lara Jr.
@github: https://github.com/RaulLara

Description: The following program partitions several important dates for
each quarter at UCSC. At UCSC there are four quarters. The partition will 
take into account the seven days of the week in a specific quarter. There
are three different remote lots, East, West, and North. The plan is to have
a running average taking based on certain hour of the day and set that to a
binning, then having that change throughout the days. Then later use weather
to predict a probability of amount of cars at a certain time. 
"""
import json
import requests
import math
import pyowm
import datetime
import random 

#The following is the free PYOWM API key
owm = pyowm.OWM('1fd0da272c8ff39ec4d9fba73e2b0e7f')

#The following is the Specific Time Variables that will set up the binning for each specific time
Fall,Winter,Spring,Summer = (0,0,0,0)
Quarters = [Fall, Winter, Spring, Summer]
TimeMo, TimeTu, TimeWe, TimeTh, TimeFr, TimeSa, TimeSu = (0,0,0,0,0,0,0)
Mo, Tu, We, Th, Fr, Sa, Su = (TimeMo, TimeTu, TimeWe, TimeTh, TimeFr, TimeSa, TimeSu)
Days = [Mo, Tu, We, Th, Fr, Sa, Su]
'''
EastRemote = [ [ er0m, er1m, er2m, er3m, er4m, er5m, er6m, er7m, erchecksm], [ er0tu, er1tu, er2tu, er3tu, er4tu, er5tu, er6tu, er7tu, erchecksm], [er0w, er1w, er2w, er3w, er4w, er5w, er6w, er7w,erchecksw], [er0th, er1th, er2th, er3th, er4th, er5th, er6th, er7th, erchecksth], [er0f, er1f, er2f, er3f, er4f, er5f, er6f, er7f, erchecksf], [er0sa, er1sa, er2sa, er3sa, er4sa, er5sa, er6sa, er7sa, ercheckssa], [er0su, er1su, er2su, er3su, er4su, er5su, er6su, er7su, ercheckssu]]
WestRemote = [ [ wr0m, wr1m, wr2m, wr3m, wr4m, wr5m, wr6m, wr7m, wrchecksm], [ wr0tu, wr1tu, wr2tu, wr3tu, wr4tu, wr5tu, wr6tu, wr7tu, wrchecksm], [wr0w, wr1w, wr2w, wr3w, wr4w, wr5w, wr6w, wr7w,wrchecksw], [wr0th, wr1th, wr2th, wr3th, wr4th, wr5th, wr6th, wr7th, wrchecksth], [wr0f, wr1f, wr2f, wr3f, wr4f, wr5f, wr6f, wr7f, wrchecksf], [wr0sa, wr1sa, wr2sa, wr3sa, wr4sa, wr5sa, wr6sa, wr7sa, wrcheckssa], [wr0su, wr1su, wr2su, wr3su, wr4su, wr5su, wr6su, wr7su,wrcheckssu]]
NorthRemote = [ [ nr0m, nr1m, nr2m, nr3m, nr4m, nr5m, nr6m, nr7m, nrchecksm], [ nr0tu, nr1tu, nr2tu, nr3tu, nr4tu, nr5tu, nr6tu, nr7tu, nrchecksm], [nr0w, nr1w, nr2w, nr3w, nr4w, nr5w, nr6w, nr7w,nrchecksw], [nr0th, nr1th, nr2th, nr3th, nr4th, nr5th, nr6th, nr7th, nrchecksth], [nr0f, nr1f, nr2f, nr3f, nr4f, nr5f, nr6f, nr7f, nrchecksf], [nr0sa, nr1sa, nr2sa, nr3sa, nr4sa, nr5sa, nr6sa, nr7sa, nrcheckssa], [nr0su, nr1su, nr2su, nr3su, nr4su, nr5su, nr6su, nr7su,nrcheckssu]]
'''

EastRemote = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
WestRemote = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
NorthRemote = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

#The following adds the current count to the average to keep an up to date average
def TakeCount(Quarter, Day, Hour, Average, CurrentCount, StdDv, Checks):
   #Sets New Average but first needs to check factors that might effect parking, such as rain
   Average = RainProbability(Quarter, Day, Hour, Average)
   
   NewAverage = (Average + CurrentCount)/(Checks + 1)
   #The variance is found using Naive Algorithm
   StandardDeviation = sqrt(StdDv + (CurrentCount - NewAverage) * (CurrentCount - Average))
   return {'Quarter' : Quarter, 'Date': [Day,Hour], 'StDv' : StandardDeviation, "CurrentCount" : NewAverage }

def RainProbability(Quarter, Date , Hour, Average):# Date format = YYYY-MM-DD
        Hour = Hour + ":00:00+00"
        #Receiving the forecast for the next few days
        SantaCruzWeather = owm.weather_at_place('Santa Cruz,US')
        forecast = owm.three_hours_forecast('Santa Cruz, US')
        #Getting the chance of rain for the hours specified
        date_to_check = Date
        date_to_check_str = Date + Hour
        
        weather_today = forecast.get_weather_at(date_to_check_str)
        if weather_today.get_status() == 'Rain' :
            Average = Average * 1.2
            
        return Average 
    
if __name__ == '__main__':
    '''Example Code to Run with made up data'''
    '''This sets up random sampling of data at a certain time with the count being 5'''
    for i1 in range(len(EastRemote)):
        for i2 in range(len(EastRemote[0])-1):
            EastRemote[i1][i2] = random.randrange(0,50)
    for i in range(len(EastRemote)):
        EastRemote[i][-1] = 5
    '''Now the count will be taken for a certain hour of Winter Quarter'''
    Date = '2018-01-23'
    NewCount = TakeCount("Winter", )    