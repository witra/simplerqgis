import os.path

from qgis.core import QgsRasterLayer


def load_raster(raster_path: str):
    layer_name = os.path.basename(raster_path)
    layer = QgsRasterLayer(raster_path, layer_name)
    if not layer.isValid():
        raise Exception("Sorry, Layer failed to load!")
    return layer


"""
def build_virtual_raster(raster_list: List[QgsRasterLayer], output_path: str):
    remove_file(output_path)
    parameters = {
        'INPUT': raster_list,
        'RESOLUTION': 2,
        'PROJ_DIFFERENCE': False,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    reproject = processing.run('gdal:buildvirtualraster', parameters)
    return reproject
"""
