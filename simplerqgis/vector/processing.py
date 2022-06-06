from simplerqgis.vector.creation import *
from typing import List, Union
from qgis import processing
from qgis.core import QgsVectorLayer, QgsFeature
from simplerqgis.utils import remove_file, get_crs
from simplerqgis.vector.utils import (transform_to_qgsvectorlayer,
                                      change_attribute_values)


def clip_vector_by_mask(input_layer: Union[str, QgsVectorLayer],
                        mask: Union[str, QgsVectorLayer],
                        output_path: str):
    """

    @param in_put:
    @param mask:
    @param output_path:
    @return:
    """
    remove_file(output_path)
    mkdir(os.path.dirname(output_path))
    input_layer = transform_to_qgsvectorlayer(input_layer)
    mask = transform_to_qgsvectorlayer(mask)
    parameters = {
        'INPUT': input_layer,
        'MASK': mask,
        'OUTPUT': output_path
    }
    clipped = processing.run('gdal:clipvectorbypolygon', parameters)
    return load_vector_layer(output_path)


def reproject_layer(input_layer: Union[str, QgsVectorLayer],
                    output_path: str, target_crs='EPSG:4326'):
    remove_file(output_path)
    mkdir(os.path.dirname(output_path))
    input_layer = transform_to_qgsvectorlayer(input_layer)
    parameters = {
        'INPUT': input_layer,
        'TARGET_CRS': target_crs,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    reproject = processing.run('native:reprojectlayer', parameters)
    return load_vector_layer(output_path)

"""
def create_point_at(geom, distance):
    feature_lenght = geom.length()
    current_distance = 0
    feats = []
    while current_distance < feature_lenght:
        point = geom.interpolate(current_distance)
        fet = QgsFeature()
        # fet.setAttributes([0, current_distance])
        fet.setGeometry(point)
        feats.append(fet)
        current_distance += distance
    return feats


def points_along_line(input_layer: QgsVectorLayer, distance):
    # source: https://gis.stackexchange.com/questions/27102/creating-equidistant-points-in-qgis
    crs_input = get_crs(input_layer)
    uri = 'Point?crs={}&index=yes'.format(crs_input)
    vector_layer, provider = temporary_vector(uri, 'Point_with_distance_{}_of_{}'.format(distance, input_layer.name()))
    # fields = {"distance": "Double"}
    # add_vector_fields(vector_layer, fields, provider)

    features = input_layer.getFeatures()
    for feature in features:
        geom = feature.geometry()
        feature_lenght = geom.length()
        if distance > feature_lenght:
            continue
        fests_point = create_point_at(geom, distance)
        provider.addFeatures(fests_point)
        vector_layer.updateExtents()
    return vector_layer


def extract_vertices(input_layer: Union[str, QgsVectorLayer],
                     output_path: str):
    input_layer = transform_to_qgsvectorlayer(input_layer)
    parameters = {
        'INPUT': input_layer,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    extracted_vertices = processing.run('native:extractvertices', parameters)
    return load_vector_layer(output_path)


def merge_vector_layer(layer_list: List[QgsVectorLayer],
                       output_path: str):
    parameters = {
        'LAYERS': layer_list,
        'CRS': get_crs(layer_list[0]),
        'OUTPUT': output_path
    }
    remove_file(output_path)
    merged_layer = processing.run('native:mergevectorlayers', parameters)
    return load_vector_layer(output_path)


def square_buffer(input_layer: Union[str, QgsVectorLayer],
                  distance: int,
                  output_path: str):
    parameters = {
        'INPUT': transform_to_qgsvectorlayer(input_layer),
        'DISTANCE': distance,
        'END_CAP_STYLE': 2,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    buffered_layer = processing.run('native:buffer', parameters)
    return load_vector_layer(output_path)


def change_attribute_column(input_layer: QgsVectorLayer, column_idx, name_prefix: str):

    Changes attribute for all rows on a columns

    features = input_layer.getFeatures()
    for f in features:
        fid = f.id()
        attrs = {column_idx: '{}_{}'.format(name_prefix, fid)}
        action = change_attribute_values(input_layer, fid, attrs)
    return action


def generate_centroids(vector_layer: QgsVectorLayer, output_path: str):
    parameters = {
        'INPUT': vector_layer,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    centroids = processing.run('native:centroids', parameters)
    return load_vector_layer(output_path)


def join_attributes(input_1: QgsVectorLayer,
                    field_1: str,
                    input_2: QgsVectorLayer,
                    field_2: str,
                    method: int,
                    output_path: str):




    parameters = {
        'INPUT': input_1,
        'FIELD': field_1,
        'INPUT_2': input_2,
        'FIELD_2': field_2,
        'METHOD': method,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    reproject = processing.run('native:joinattributestable', parameters)
    return load_vector_layer(output_path)


def join_by_spatial(base: QgsVectorLayer,
                    join: QgsVectorLayer,
                    predicate: int,  # default overlap
                    method: int,
                    output_path: str
                    ):


    parameters = {
        'INPUT': base,
        'JOIN': join,
        'PREDICATE': predicate,
        'METHOD': method,
        'JOIN_FIELDS': 'full_id',
        'OUTPUT': output_path
    }
    remove_file(output_path)
    reproject = processing.run('native:joinattributesbylocation', parameters)
    if output_path != 'memory:':
        output_layer = reproject['OUTPUT']
    output_layer = load_vector_layer(output_path)
    return output_layer


def buffer(input_layer: QgsVectorLayer, distance: float, output_path: str):
    parameters = {
        'INPUT': input_layer,
        'DISTANCE': distance,
        'OUTPUT': output_path
    }
    remove_file(output_path)
    buffer = processing.run('native:buffer', parameters)
    print(buffer)
    if output_path != 'memory:':
        output_layer = buffer['OUTPUT']
    return load_vector_layer(output_path)

"""
