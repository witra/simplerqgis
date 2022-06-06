from simplerqgis.initializations import set_qgsapplication_instance
from simplerqgis.vector.creation import *


# application = set_qgsapplication_instance()
# print(os.getcwd())


def test_temporary_vector():
    vl, pr = temporary_vector('Point', 'temp')
    assert isinstance(vl, QgsVectorLayer)
    assert isinstance(pr, QgsVectorDataProvider)


def test_load_vector_layer():
    path = '../../tiny_data/vector/highway_houston.shp'
    vl = load_vector_layer(path)
    assert isinstance(vl, QgsVectorLayer)


"""
def test_load_csv_layer():
    parent_cwd = os.path.dirname(os.getcwd())
    # print(parent_cwd)
    path = '../../tiny_data/prediction.csv'
    vl = load_csv_layer(path)
    assert isinstance(vl, QgsVectorLayer)
"""


def test_write_vector():
    path = '../../tiny_data/vector/highway_houston.shp'
    vl = load_vector_layer(path)
    # write_path = tmpdir.join('test_write.gpkg')
    write_path = '../../tiny_data/inter/test_write.gpkg'
    w_vl = write_vector(vl, write_path)
    assert os.path.isfile(write_path) is True
