from simplerqgis.raster.creation import *
from simplerqgis.initializations import set_qgsapplication_instance


def test_load_raster():
    raster_path = '../../tiny_data/raster/103001006FCDF300.tif'
    rl = load_raster(raster_path)
    assert isinstance(rl, QgsRasterLayer)

"""
def test_build_virtual_raster():
    pass
"""
