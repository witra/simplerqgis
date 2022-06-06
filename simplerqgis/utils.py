import os
from qgis.core import QgsApplication
from qgis import processing
from simplerqgis.initializations import *


def remove_file(path):
    if os.path.isfile(path):
        os.remove(path)


def mkdir(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)


def get_crs(layer):
    """
    return crs code
    """
    return layer.crs().authid()


def algorithm_list():
    app = initialize_processing()
    for alg in QgsApplication.processingRegistry().algorithms():
        print("{}:{} --> {}".format(alg.provider().name(), alg.name(), alg.displayName()))


def algorithm_help(alg_id: str):
    app = initialize_processing()
    processing.algorithmHelp(alg_id)
