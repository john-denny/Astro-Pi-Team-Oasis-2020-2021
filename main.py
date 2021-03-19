# Team Oasis Astro Pi project 2021
from ephem import readtle, degree
from time import sleep
from sense_hat import SenseHat
from datetime import datetime
from logzero import logger, logfile
from csv import writer
import csv
from picamera import PiCamera

NumberOfRuns = 1
PhotoNumber = 0
TopHat = SenseHat()
PhotoTaker = PiCamera()
redAWB = 1
blueAWB = 0.5
customGains = (redAWB, blueAWB)
PhotoTaker.awb_mode = "off"
PhotoTaker.awb_gains = customGains
PhotoTaker.start_preview()
PhotoTaker.resolution = (1920, 1080)
logfile("OasisLogfile.log")

# TLE DATA (From Norad) - https://www.celestrak.com/NORAD/elements/stations.txt
Title = "ISS ZARYA"
LineI = "1 25544U 98067A   21025.32718219  .00001091  00000-0  28047-4 0  9999"
LineII = "2 25544  51.6462 329.3197 0002267 288.7769 172.4159 15.48884919266453"
# Note name of variable is Dawn to Stop Confusion and Zarya means Dawn in Russian
DawnTLE = readtle(Title, LineI, LineII)


# Gather date, time, latitude and longitude
def DataGatherer():
    TopHat_data = []
    TopHat_data.append(datetime.now())
    TopHat_data.append(latitude)
    TopHat_data.append(longitude)
    return TopHat_data

# Gather photo with incremental file name
def TakePhoto():
    PhotoTaker.capture("Photo" + str(PhotoNumber) + ".jpeg")

# Creates a data file with headers containing latitude, longitude and datetime
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    header = ('datetime', 'lat', 'lon')
    writer.writerow(header)

# Runs the program 226 times
while NumberOfRuns <= 226:
    DawnTLE.compute()
    latitude = DawnTLE.sublat/degree
    longitude = DawnTLE.sublong/degree
    data = DataGatherer()
    print(DataGatherer())
    NumberOfRuns = NumberOfRuns + 1
    PhotoNumber = PhotoNumber + 1
    sleep(46)
    logger.info(f"iteration {PhotoNumber}") # Adds the latitude, longitude and datetime data to the csv file
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        TakePhoto()
