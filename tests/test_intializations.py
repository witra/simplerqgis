import pytest
from simplerqgis.initializations import *
from qgis.core import QgsApplication


def test_get_qgis_path():
    qgis_path = get_qqis_path()
    assert type(qgis_path) == str


def test_set_qgsapplication_instance():
    app = type(set_qgsapplication_instance())
    app_true = type(QgsApplication([], True))
    assert app == app_true


def test_initialise_qgis_resource():
    app = type(initialise_qgis_resource())
    app_true = type(QgsApplication([], True))
    assert app == app_true
