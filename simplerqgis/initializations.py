from qgis.core import (QgsApplication)
from processing.core.Processing import Processing
import subprocess


def get_qqis_path():
    stdout = str(subprocess.run(['where', 'qgis'],
                                stdout=subprocess.PIPE).stdout)
    qgis_path = stdout[2:-5]
    return qgis_path


def set_prefix(qgis_path):
    QgsApplication.setPrefixPath(qgis_path, True)


def set_qgsapplication_instance():
    app1 = QgsApplication([], True)
    app1.initQgis()
    return app1


def initialise_qgis_resource():
    qgis_path = get_qqis_path()
    set_prefix(qgis_path)
    application = set_qgsapplication_instance()
    return application


def initialize_processing():
    app2 = Processing()
    return app2.initialize()

"""
from vector.creation import load_vector_layer
import os
if __name__ == '__main__':
    app = initialise_qgis_resource()
    print(type(app))
    print(os.getcwd())
    houston_highway_path = "../tiny_data/vector/highway_houston.shp"
    h_highway = load_vector_layer(houston_highway_path)
    print('success to initialise qgis resources')
"""
