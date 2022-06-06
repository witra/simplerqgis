from qgis.core import QgsRasterLayer, QgsFeature
from qgis import processing
from simplerqgis.vector.creation import temporary_vector
from src.utils.utils import check_existing
from src.utils.gis.utils import get_crs


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

def reproject_raster(raster_layer: QgsRasterLayer, target_crs: str, output_path: str):
    check_existing(output_path)
    parameters = {
    'INPUT': raster_layer,
    'SOURCE_CRS': get_crs(raster_layer),
    'TARGET_CRS': target_crs,
    'OUTPUT': output_path
    }
    check_existing(output_path)
    reproject = processing.run('gdal:warpreproject', parameters)
    return reproject

def clip_raster_by_mask(raster_layer, mask, output_path):
    parameters = {
    'INPUT': raster_layer,
    'MASK' : mask,
    'NO_DATA': -9999,
    'OUTPUT': output_path
    }
    check_existing(output_path)
    clipped = processing.run('gdal:cliprasterbymasklayer', parameters)
    return clipped

def clip_raster_by_feature(raster: QgsRasterLayer, feature: QgsFeature, out_dir:str):
    """
    clip raster using the iterated feature
    """
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    fid = feature.id()
    uri = 'multipolygon'
    temp_layer, provider = temporary_vector(uri, 'temp')
    out_path = out_dir + '{}_{}.tif'.format(raster.name(), fid)
    clipped = clip_raster_by_mask(raster, temp_layer, out_path)
    return clipped
