import os
import sys


package_dir = os.path.dirname(__file__)
repository_dir = package_dir
for level in range(2):
    repository_dir = os.path.dirname(repository_dir)

library_dir = os.path.join(
    repository_dir,
    "lib",
    "pyblish-suite",
    "pyblish-qml")

sys.path.insert(0, library_dir)

import pyblish_qml
sys.modules[__name__] = pyblish_qml
reload(pyblish_qml)