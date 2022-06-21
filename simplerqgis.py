"""Main module."""
import os
from qgis.core import *
from simplerqgis.initializations import *
# from initializations import initialize_qgis_resource
from simplerqgis.vector.creation import load_vector_layer

if __name__ == '__main__':
    print('beginning')
    app = initialize_qgis_resource()
    app2 = initialize_processing()
    print('type of app', type(app))
    print('current working dir', os.getcwd())
    houston_highway_path = './tiny_data/vector/Harvey_ROI.shp'
    h_highway = load_vector_layer(houston_highway_path)
    print('success to initialise qgis resources')
