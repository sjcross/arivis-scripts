# coding: utf-8
# Note: Due to differences in how ImageJ and Arivis store polygons (e.g. ROIs), 
# Arivis will increase ROI sizes by ~1 px
import re

from arivis import App
from arivis_core import Point2D
from arivis_objects import Polygon, Segment, Store
from roifile import roiread
from zipfile import ZipFile

# Parameters
zip_path = ""

# Getting core components
viewer = App.get_active_viewer()
document = viewer.get_document()
imageset = viewer.get_imageset()

# Creating a new object store
object_store = document.get_store(imageset, Store. DOCUMENT_STORE)
segments = {}

pattern = re.compile('^ID([0-9]+)_TR([\\-0-9]+)_T([0-9]+)_Z([0-9]+).roi$')
  
# Loading ROI files
# We use ZipFile as the roi filename contains slice and timepoint
with ZipFile(zip_path, "r") as zip:
  count = 1
  total = len(zip.infolist())
  for file in zip.namelist():
    match = pattern.match(file)
    ID = match.groups()[0]
    timepoint = int(match.groups()[2]) - 1
    slice = int(match.groups()[3]) - 1
    
    if not ID in segments.keys():
      segment = Segment()
      segment.set_timepoint(timepoint)
      segments[ID] = segment
    
    segment = segments[ID]
    
    roi = roiread(file)
    #add_roi(roi, segment, slice, timepoint)
    
    points = []
    for coord in roi.coordinates():
      points.append(Point2D(int(coord[0]),int(coord[1])))
  
    polygon = Polygon()
    polygon.set_contour(points)
  
    segment.add_polygon(polygon, slice)
    
    print(f"Loaded {count} of {total} rois ({100*count/total:.2f}%)")
    count = count + 1

# Adding segments to object store
for segment in segments.values():
  object_store.add_object(segment)

