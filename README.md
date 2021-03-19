# Astro Pi 2020/21 Team Oasis
 Astro Pi submission for 2020/2021 pending results

# The Idea
The Idea for the project is that we will use the Pi NoIR camera on the International Space Station to measure crop health and compare that with the Area's social climate (E.g Drought, War Etc).

# What we used
- Raspberry Pi 3
- Pi Sense Hat
- Pi Noir V2 camera
- XRDP (Not Necessary but very useful) https://pimylifeup.com/raspberry-pi-remote-desktop/
- Cfasties Colormap for NDVI https://publiclab.org/notes/cfastie/08-26-2014/new-ndvi-colormap

# Some Assumptions We Made
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