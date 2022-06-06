from qgis.core import (QgsApplication)
import subprocess


def get_qqis_path():
    stdout = str(subprocess.run(['where', 'qgis'],
                                stdout=subprocess.PIPE).stdout)
    qgis_path = stdout[2:-5]
    return qgis_path


def set_prefix(qgis_path):
    QgsApplication.setPrefixPath(qgis_path, True)


def set_qgsapplication_instance():
    app1 = QgsApplication([], True)
    app1.initQgis()
    return app1


def initialise_qgis_resource():
    qgis_path = get_qqis_path()
    set_prefix(qgis_path)
    app = set_qgsapplication_instance()
    return app

if __name__ == '__main__':
    app = initialise_qgis_resource()
    print('success to initialise qgis resources')
    print(type(app))

