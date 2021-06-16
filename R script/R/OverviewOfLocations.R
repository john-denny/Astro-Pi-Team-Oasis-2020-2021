#
# Plot co-ordinates of ISS images taken
#
# library(tidyverse)
#library(ggmap)
library(sf)
library(mapview)

ImageLocTimeInfoFile <- file.choose()
ImageLocTimeInfo <- read.csv(ImageLocTimeInfoFile, header = TRUE)

locations_sf <- st_as_sf(ImageLocTimeInfo, coords = c("lon", "lat"), crs = 4326)
mapview(locations_sf)
