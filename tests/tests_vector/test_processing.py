import os.path

from simplerqgis.initializations import *
from simplerqgis.vector.processing import *

application = set_qgsapplication_instance()
process = initialize_processing()


def test_clip_vector_by_mask():
    obj = './tiny_data/vector/Harvey_ROI.shp'
    mask = './tiny_data/vector/Houston_area_prediction.shp'
    out = './tiny_data/inter/test_clip.gpkg'
    clipped = clip_vector_by_mask(obj, mask, out)
    assert os.path.isfile(out) is True
    assert isinstance(clipped, QgsVectorLayer)


def test_reproject_layer():
    obj = './tiny_data/vector/Harvey_ROI.shp'
    target_crs = 'EPSG:3857'
    out = './tiny_data/inter/test_reproject.gpkg'
    reproject = reproject_layer(obj, out, target_crs)
    assert os.path.isfile(out) is True
    assert isinstance(reproject, QgsVectorLayer)
    assert get_crs(reproject) == target_crs


def test_create_point_at():
    pass


def test_points_along_line():
    pass


def test_extract_veritices():
    pass


def test_merge_vector_layer():
    pass


def test_square_buffer():
    pass


def test_change_attributes_columns():
    pass


def test_generate_centroids():
    pass


def test_join_attributes():
    pass


def test_join_by_spatial():
    pass


def test_buffer():
    pass

