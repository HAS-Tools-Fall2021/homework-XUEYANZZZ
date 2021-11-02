# %%
import os 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.colors import ListedColormap
import seaborn as sns
import geopandas as gpd
import earthpy as et
from shapely import coords, geometry

# %% ----------------------Training 1----------------------
# Setting plotting style for the notebook
sns.set_style("white")
sns.set(font_scale=1.5)

# Set working dir and get data
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

# Import the data
sjer_roads_path = os.path.join("data", "spatial-vector-lidar", "california",
                               "madera-county-roads", "tl_2013_06039_roads.shp")

sjer_roads = gpd.read_file(sjer_roads_path)

sjer_aoi_path = os.path.join("data", "spatial-vector-lidar", "california",
                               "neon-sjer-site", "vector_data", "SJER_crop.shp")

sjer_aoi = gpd.read_file(sjer_aoi_path)

# View the coordinate reference system of both layers
print(sjer_roads.crs)
print(sjer_aoi.crs)

# Reproject the aoi to match the roads layer
sjer_aoi_wgs84 = sjer_aoi.to_crs(epsg=4269)

# %% Plotting
fig, ax = plt.subplots(figsize=(12, 8))
sjer_roads.plot(cmap='Greys', ax=ax, alpha=.5)
sjer_aoi_wgs84.plot(ax=ax, markersize=10, color='r')
ax.set_title("Madera County Roads with SJER AOI")

# %% Read US boundary file
# Import data into geopandas dataframe
state_boundary_us_path = os.path.join("data", "spatial-vector-lidar", 
                                      "usa", "usa-states-census-2014.shp")

state_boundary_us = gpd.read_file(state_boundary_us_path)
type(state_boundary_us)
state_boundary_us.crs
state_boundary_us.head()

# %% Plot the US boundary data
fig, ax = plt.subplots()
state_boundary_us.plot(ax=ax, facecolor='white', edgecolor='black')
ax.set(title="Map of Continental US State Boundaries\n United States Census Bureau Data")
plt.axis('equal')
ax.set_axis_off()

plt.show()
# %% Add a boundary layer of the US
county_boundary_us_path = os.path.join("data", "spatial-vector-lidar", 
                                       "usa", "usa-boundary-dissolved.shp")

county_boundary_us = gpd.read_file(county_boundary_us_path)

type(county_boundary_us)
county_boundary_us.columns
county_boundary_us.head()
county_boundary_us.crs

# Plot data
fig, ax = plt.subplots(figsize=(12, 7))
county_boundary_us.plot(ax=ax, alpha=1, edgecolor="black",
                        color="white", linewidth=1)

state_boundary_us.plot(ax=ax, color="indigo", edgecolor="white",
                  linewidth=1)
                
ax.set_axis_off()
plt.show()

# %% Add the SJER to my map
# Reproject sjer to crs of country_bounary
sjer_aoi_project = sjer_aoi.to_crs(county_boundary_us.crs)
fig, ax = plt.subplots(figsize=(6, 6))

state_boundary_us.plot(ax=ax, color="white", edgecolor="black")
county_boundary_us.plot(ax=ax, edgecolor="black", color="white",
                        linewidth=3, alpha=0.8)


sjer_aoi_project.plot(ax=ax, color="springgreen", edgecolor="r")
ax.set(title='San Joachin Experimental Range \n Area of interest (AOI)')

#ax.set_axis_off()
ax.set(xlim=[-125, -116], ylim=[35, 40])
# Turn off axis
ax.set(xticks=[], yticks=[])
plt.show()

# %% Convert a small polygon to a polygon cetroid (point)
AOI_point = sjer_aoi_project["geometry"].centroid
sjer_aoi_project["geometry"].centroid.plot()

# Plot again

fig, ax = plt.subplots()
state_boundary_us.plot(ax=ax, linewidth=1, edgecolor="black")

county_boundary_us.plot(ax=ax, alpha=0.7, edgecolor="black", color="white",
                        linewidth=3)

AOI_point.plot(ax=ax, markersize=80, color='purple', marker='*')

ax.set(title="Map of Continental US State Boundaries \n with SJER AOI")

ax.set_axis_off()
# %% ----------------------Training 2----------------------
# Load the box module from shapely to create box objects
# Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.colors import ListedColormap
import geopandas as gpd

from shapely.geometry import box
import earthpy as et
import seaborn as sns

# Ignore warning about missing/empty geometries
import warnings
warnings.filterwarnings('ignore', 'GeoSeries.notna', UserWarning)

# Adjust plot font sizes
sns.set(font_scale=1.5)
sns.set_style("white")

# Set working dir & get data
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
# %% How to clip shapefiles in python
# Import all of your data at the top of your notebook to keep things organized.
country_boundary_us_path = os.path.join("data", "spatial-vector-lidar", 
                                        "usa", "usa-boundary-dissolved.shp")
country_boundary_us = gpd.read_file(country_boundary_us_path)

state_boundary_us_path = os.path.join("data", "spatial-vector-lidar", 
                                      "usa", "usa-states-census-2014.shp")
state_boundary_us = gpd.read_file(state_boundary_us_path)

pop_places_path = os.path.join("data", "spatial-vector-lidar", "global", 
                               "ne_110m_populated_places_simple", "ne_110m_populated_places_simple.shp")
pop_places = gpd.read_file(pop_places_path)

print("country_boundary_us", country_boundary_us.crs)
print("state_boundary_us", state_boundary_us.crs)
print("pop_places", pop_places.crs)

# Plot
fig, ax = plt.subplots()
county_boundary_us.plot(alpha=0.5, ax=ax)
state_boundary_us.plot(cmap='Greys', ax=ax, alpha=0.5)
pop_places.plot(ax=ax)

plt.axis('equal')
ax.set_axis_off()
plt.show()

# %% Clip the points shapefile in python using geopandas
points_clip = gpd.clip(pop_places, country_boundary_us)

points_clip[['name', 'geometry', 'scalerank', 'natscale', ]].head()

# Plot the data
fig, ax = plt.subplots()

country_boundary_us.plot(alpha=1, color="white", edgecolor="black", ax=ax)

state_boundary_us.plot(cmap='Greys', ax=ax, alpha=0.5)

points_clip.plot(ax=ax, column='name')

ax.set_axis_off()
plt.axis('equal')

# Label each point
points_clip.apply(lambda x: ax.annotate(s=x['name'],
                                        xy=x.geometry.coords[0],
                                        xytext=(6,6), textcoords="offset points",
                                        backgroundcolor="white"),
                  axis=1)

plt.show()

# %% Clip roads with simplified clip data
# Open the roads layer
ne_roads_path = os.path.join("data", "spatial-vector-lidar", "global", 
                             "ne_10m_roads", "ne_10m_roads.shp")
ne_roads = gpd.read_file(ne_roads_path)

# Are both layers in the same CRS?
if (ne_roads.crs == country_boundary_us.crs):
    print("Both layers are in the same crs!",
          ne_roads.crs, country_boundary_us.crs)

country_boundary_us_sim = country_boundary_us.simplify(.2, preserve_topology=True)

# Clip data
ne_roads_clip = gpd.clip(ne_roads, country_boundary_us_sim)

# Ignore missing/empty geometries
ne_roads_clip = ne_roads_clip[~ne_roads_clip.is_empty]

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

ne_roads.plot(ax=ax1)
ne_roads_clip.plot(ax=ax2, column='type', legend=True)

ax1.set_title("Unclipped roads")
ax2.set_title('clipped roads')

plt.axis('equal')
plt.show()


# %% Create a customized legend based on dictionaries
road_attrs = {'Beltway': ['black', 2],
              'Secondary Highway': ['grey', .5],
              'Road': ['grey', .5],
              'Bypass': ['grey', .5],
              'Ferry Route': ['grey', .5],
              'Major Highway': ['black', 1]}

# Plot 
fig, ax = plt.subplots(figsize=(12, 8))

for ctype, data in ne_roads_clip.groupby('type'):
    data.plot(color=road_attrs[ctype][0],
              label=ctype,
              ax=ax,
              linewidth=road_attrs[ctype][1])

country_boundary_us.plot(ax=ax, alpha=1, color="white", edgecolor="black")

ax.legend(frameon=False, loc=(0.1, -0.1))

ax.set_title("United States Roads by Type", fontsize=25)
ax.set_axis_off()

plt.axis('equal')
plt.show()
# %%
