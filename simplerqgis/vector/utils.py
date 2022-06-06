from simplerqgis.vector.creation import load_vector_layer
from qgis.core import QgsVectorLayer, QgsField
from typing import Dict, List


def transform_to_qgsvectorlayer(input_layer):
    if type(input_layer) == str:
        input_type = load_vector_layer(input_layer)
    elif type(input_layer) == QgsVectorLayer:
        input_type = input_layer
    else:
        raise Exception('Sorry, your input is not either string nor QgsVectorLayer format')
    return input_type

"""
def add_vector_fields(vector_layer: QgsVectorLayer,
                      fields: dict, provider=None):
    if provider is None:
        provider = vector_layer.dataProvider()
    fields_args = [QgsField(key, eval('QVariant.{}'.format(fields[key]))) for key in
                   fields]
    provider.addAttributes(fields_args)
    vector_layer.updateFields()


def get_field_name(vector_layer: QgsVectorLayer):
    return vector_layer.fields().names()


def field_index(vector_layer: QgsVectorLayer, field_name: str):
    return vector_layer.fields().indexOf(field_name)


def delete_fields(vector_layer: QgsVectorLayer, field_index: List[int]):
    vector_layer.dataProvider().deleteAttributes(field_index)
    vector_layer.updateFields()


def change_attribute_values(vector_layer: QgsVectorLayer, fid: int, attrs: Dict[int, any]):
    vector_layer.dataProvider().changeAttributeValues({fid: attrs})
    vector_layer.updateFields()

"""
