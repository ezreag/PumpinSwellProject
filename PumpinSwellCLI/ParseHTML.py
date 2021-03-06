# Author: Ezra Aguimatang <ezreag>
# Date: 03.31.2022

#Given the URL, this file parses raw HTML and prints desired surf conditions

from CLI import *

class parsingInfo:
    def __init__(self, soup):
        self.soup = soup

    def getcurrtemp(self):
        #prints current date's average temperature
        tempstr = str(self.soup.find('div', attrs={'class':'wx-icon-temp'}))
        if "°" in tempstr:
            startpos = tempstr.find(">") + 1
            endpos = tempstr.find("</")
            print("Avg Temperature: ", tempstr[startpos:endpos], "\n")
        else:
            print("No temp forcast for today :(\n")

    def getcurrwind(self):
        #prints current date's wind direction and avg wind speed
        windstr = str(self.soup.find('div', attrs={'class':'wx-icons-wind-desc'}))
        if "mph" in windstr:
            startpos = windstr.find(">") + 1
            endpos = windstr.find("<i") - 1
            print("Wind Direction:  ", windstr[startpos:endpos])

            windspeedstr = windstr[endpos:len(windstr)]
            if "arrow" in windspeedstr:
                startpos = windspeedstr.find("arrow") + 17
            else:
                startpos = windspeedstr.find("/i>") + 3
            endpos = windspeedstr.find("mph") + 3
            print("Avg Wind Speed: ", windspeedstr[startpos:endpos], "\n")
        elif "Calm" in windstr:
            print("Avg Wind Speed:  ", "Calm", "\n")
        else:
            print("No wind forcast for today :(\n")

    def getbuoydata(self):
        #prints buoy number and data
        buoystr = str(self.soup.find('div', attrs={'class':'wx-icon-buoy-data'}))
        if "@" in buoystr:
            buoynamepos = buoystr.find("Buoy ")
            buoystr = buoystr[buoynamepos:len(buoystr)]
            endstr = buoystr.find("<")
            print("Buoy Name: ", buoystr[0:endstr])

            startpos = buoystr.find("<div>") + 5
            endpos = buoystr.find("sec") + 3
            print("Buoy Data: ", buoystr[startpos:endpos], "\n")
        else:
            print("No buoy data for today :(\n")

    def gettidedata(self):
        #prints tide data
        tidestr = str(self.soup.find('div', attrs={'class':'wx-icon-tide-data'}))
        if ("LOW" or "HIGH") in tidestr:
            tidelist = tidestr.rsplit("\n")
            lowstr = tidelist[1]
            highstr = tidelist[2]
            print("LOW TIDE:  ", lowstr[lowstr.find(":")-2:-6])
            print("HIGH TIDE: ", highstr[highstr.find(":")-2:-6], "\n")
        else:
            print("No tide data for today :(\n")
        
    def getwatertemp(self):
        #prints water temp data
        watertempstr = str(self.soup.find('div', attrs={'class':'wx-icon-water-data'}))
        if "°" in watertempstr:
            watertemplist = watertempstr.rsplit("\n")
            tempstr = watertemplist[1]
            suitstr = watertemplist[2]
            print("Avg Water Temp:   ", watertemplist[1][tempstr.find(">")+1:-6])
            print("Recommended Suit: ", watertemplist[2][suitstr.find(">")+1:-6], "\n")
        else:
            print("No water temp data for today :(\n")

    def getwavecond(self):
        #prints wave height
        wavestr = str(self.soup.find('div', attrs={'class':'graph-data-wave-height'}))
        if "ft" in wavestr:
            waveheighpos = wavestr.find("ght") + 5
            waveheighstr = wavestr[waveheighpos:-6]
            print("Wave Height:    ", waveheighstr)
        else:
            print("No wave height data for today :(\n")

        #prints wave condition
        wavecondstr = str(self.soup.find('div', attrs={'class':'graph-data-wave-cond'}))
        wavecondstr = wavecondstr[wavecondstr.find(">")+1:-6]
        if wavecondstr == "CHOPPY" or wavecondstr == "FAIR" or wavecondstr == "CLEAN":
            print("Wave Condition: ", wavecondstr, "\n")
        else:
            print("No wave condition data for today :(\n")

""""""""""""

#first draft of getcurrtemp
''''
def getcurrtemp():
    degreessymb = "°"
    for i in range(0, len(tempstr)):
        if tempstr[i] == degreessymb:
            print("Avg Temperature Today: ",tempstr[i-2:i+1])
        elif i == len(tempstr):
            print("No temp forcast for today :(")
'''
#first draft of getcurrwind
'''
f = ">"
windstr = str(soup.find('div', attrs={'class':'wx-icons-wind-desc'}))
for i in range(0, len(windstr)):
    if windstr[i] == f:
        print("Wind Direction Today:  ", windstr[i+1:i+4])
        newwindstr = windstr[i+5:len(windstr)]
        mphpos = newwindstr.find("mph")
        firstmph = newwindstr[mphpos-2]
        if firstmph == "1" or firstmph == "2"\
            or firstmph == "3" or firstmph == "4"\
                or firstmph == "5" or firstmph == "6"\
                    or firstmph == "7" or firstmph == "8"\
                        or firstmph == "9":
            print("Avg Wind Speed Today:  ", newwindstr[mphpos-2:mphpos+3])
        else:
            print("Avg Wind Speed Today:  ", newwindstr[mphpos-1:mphpos+3])
        break
    elif i == len(windstr):
        print("No wind forcast for today :(")
'''