import pytest
import os

from qgis.core import QgsRasterLayer
from simplerqgis.utils import get_crs
from simplerqgis.raster.processing import reproject_raster
from simplerqgis.raster.creation import load_raster
from simplerqgis.initializations import initialize_processing, initialise_qgis_resource


app1 = initialise_qgis_resource()
app2 = initialize_processing()


@pytest.fixture(scope='function')
def raster_layer():
    raster_path = '../../tiny_data/raster/ORIG_ID_Houston_14.tif'
    return load_raster(raster_path)


def test_reproject_raster(raster_layer):
    target_crs = 'EPSG:3857'
    out = '../../tiny_data/inter/test_reproject.tif'
    reproject = reproject_raster(raster_layer, target_crs, out)
    assert os.path.isfile(out) is True
    assert isinstance(reproject, QgsRasterLayer)
    assert get_crs(reproject) == target_crs

"""
def test_clip_raster_by_mask():
    pass


def test_clip_raster_by_feature():
    pass
"""
