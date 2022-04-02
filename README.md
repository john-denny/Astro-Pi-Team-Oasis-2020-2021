# Astro Pi 2020/21 Team Oasis


## The Idea
The Idea for the project is that we will use the Pi NoIR camera on the International Space Station to measure crop health and compare that with the Area's social climate (E.g Drought, War Etc).

## What we used
- Raspberry Pi 3
- Pi Sense Hat
- Pi Noir V2 camera
- XRDP (Not Necessary but very useful) https://pimylifeup.com/raspberry-pi-remote-desktop/
- Cfasties Colormap for NDVI https://publiclab.org/notes/cfastie/08-26-2014/new-ndvi-colormap

## Some Assumptions We Made
- We are assuming that we are 410km from the ground
- We are assuming that the camera is moving horizontally at 7.66km/s
- We are assuming that the camera on the ISS is using the V1 pi NoIR camera with the OmniVision OV5647 sensor
- We are assuming that the camera's vertical FOV is 41.41 +/- 0.11 degrees and its horizontal FOV is 53.50 +/- 0.13 degrees
- Based on the Assumptions above we assert that the horizontal size of a photo is approximately 408km

We set the time to ~10% less than how long it would take for the ISS to travel 408km which we estimated to be 46 seconds
We also set the program to run for just under 3 hours by running our loop 226 times 

Each line in the CSV corresponds to a photo the first line of data (line 2 because of headings) corresponds to photo 1 and so on. 

We haven't gotten confirmation of flight status yet but I will update the page when We
Thank you and Stay safe! 
Best, John and Team

### Update - We got it!
We got flight status on the 6th of April 2021! We are delighted!

# Analysis

### Mapping Script
We used this script to analyze the locations of the photos. Open the .rproj in R studio for the easiest use. Note: we used this after we got our data back.


### Applying colormaps 
- We used Fiji (ImageJ) to analyze the photos and apply LUTs (Lookup Tables)
- We used CFasties colormap (link above)

# Output
You can find the output of our code which we received back from ESA in the Output/ folder, this contains both images and files like the logfile and datafile

# The Paper 
- We wrote our paper about the effects of urbanisation on Vegetation health in Japan (As that is were we had the most photos) 
- The European Space Agency has rules about font, number of pages, wordcount etc. You can find the rules we had to obey in Paper/rules.pdf
- You can find the paper itself in Paper/Team Oasis Github.docx