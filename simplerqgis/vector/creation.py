import os
from qgis.core import *
from simplerqgis.utils import mkdir, remove_file


def temporary_vector(uri: str, layer_name: str):
    """
    This function define the vector by making use memory provider for
    @param uri:
    @param layer_name:
    @return:
    """
    provider_library = 'memory'
    vector_layer = QgsVectorLayer(uri, layer_name, provider_library)
    provider = vector_layer.dataProvider()
    if not vector_layer.isValid():
        raise Exception("Sorry, Layer failed to load!")
    return vector_layer, provider


def load_vector_layer(path: str):
    """
    This function is to load the vector layer.
    parameters:

    """
    layer_name = os.path.basename(path)
    layer = QgsVectorLayer(path, layer_name, 'ogr')
    if not layer.isValid():
        raise Exception("Sorry, Layer failed to load!")
    return layer


def load_csv_layer(path: str):
    """
    This function is to load the vector layer.
    parameters:

    """
    layer_name = os.path.basename(path)
    uri = str('file:///' + path + '?delimiter=,')
    layer = QgsVectorLayer(uri, layer_name, 'delimitedtext')
    if not layer.isValid():
        raise Exception("Sorry, Layer failed to load!")
    return layer

"""
def load_to_MapLayerRegistry(vector_layer: QgsVectorLayer):
    return QgsMapLayerRegistry.instance().addMapLayer(vector_layer)
"""


def write_vector(vector_layer: QgsVectorLayer, write_path: str):
    remove_file(write_path)
    mkdir(os.path.dirname(write_path))
    save_option = QgsVectorFileWriter.SaveVectorOptions()
    transform_context = QgsProject.instance().transformContext()
    QgsVectorFileWriter.writeAsVectorFormatV2(vector_layer,
                                              write_path,
                                              transform_context,
                                              save_option)
    return load_vector_layer(write_path)
