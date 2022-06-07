"""Main module."""
import os
from simplerqgis.initializations import initialize_qgis_resource
# from initializations import initialize_qgis_resource
from simplerqgis.vector.creation import load_vector_layer

if __name__ == '__main__':
    app = initialize_qgis_resource()
    print(type(app))
    print(os.getcwd())
    houston_highway_path = "./tiny_data/vector/highway_houston.shp"
    h_highway = load_vector_layer(houston_highway_path)
    print('success to initialise qgis resources')
