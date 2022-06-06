import pytest
from simplerqgis.initializations import get_qqis_path, set_qgsapplication_instance
from qgis.core import (QgsApplication)


def test_get_qgis_path():
    qgis_path = get_qqis_path()
    assert type(qgis_path) == str


def test_set_qgsapplication_instance():
    app = type(set_qgsapplication_instance())
    app_true = type(QgsApplication([], True))
    assert app == app_true
