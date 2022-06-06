from qgis.core import QgsRasterLayer
from simplerqgis.utils import check_existing
from typing import List
from qgis import processing


def load_raster(raster_path: str, layer_name:str):
    layer = QgsRasterLayer(raster_path, layer_name)
    if not layer.isValid():
        raise Exception("Sorry, Layer failed to load!")
    return layer


def build_virtual_raster(raster_list: List[QgsRasterLayer], output_path: str):
    check_existing(output_path)
    parameters = {
        'INPUT': raster_list,
        'RESOLUTION': 2,
        'PROJ_DIFFERENCE': False,
        'OUTPUT': output_path
    }
    check_existing(output_path)
    reproject = processing.run('gdal:buildvirtualraster', parameters)
    return reproject
