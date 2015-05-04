#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import re

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper

try:
    import pyensae
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae

try:
    import pymmails
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymmails

try:
    import pyrsslocal
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyrsslocal


from pyquickhelper import fLOG, get_temp_folder
from pyquickhelper.jenkinshelper import JenkinsExt
from src.ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server


class TestJenkins(unittest.TestCase):

    def test_jenkins_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        js = JenkinsExt('http://machine:8080/', "user", "password", mock=True)

        if sys.platform.startswith("win"):
            res = setup_jenkins_server(js,
                                       anaconda=r"C:\\Anaconda3",
                                       anaconda2=r"C:\\Anaconda2",
                                       winpython=r"C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                                       fLOG=fLOG,
                                       overwrite=True,
                                       location=r"c:\\jenkins\\pymy",
                                       prefix="_node_")
        else:
            modules=[("pyquickhelper", "H H(10-11) * * 0"),
                  ["pymyinstall" ],
                  ["pymyinstall [anaconda] [update]", "pymyinstall [anaconda2] [update27]"],
                  ["pyquickhelper [anaconda]",  "pyquickhelper [27] [anaconda2]"],
                  ["pyensae", ],
                  ["pymmails", "pysqllike", "pyrsslocal", "pymyinstall [27] [anaconda2]",
                   "python3_module_template", "pyensae [anaconda]", ],
                  ["pymmails [anaconda]", "pysqllike [anaconda]", "pyrsslocal [anaconda]",
                   "python3_module_template [anaconda]", "python3_module_template [27] [anaconda2]",
                   "pymyinstall [all]"],
                  # actuariat
                  [("actuariat_python", "H H(12-13) * * 0") ],
                  ["actuariat_python [anaconda]"],
                  # code_beatrix
                  [("code_beatrix", "H H(14-15) * * 0")],
                  ["code_beatrix [anaconda]"],
                  # teachings
                  ("ensae_teaching_cs", "H H(15-16) * * 0"),
                  ["ensae_teaching_cs [anaconda]"],
                  ["ensae_teaching_cs [notebooks]" ],
                  ["ensae_teaching_cs [anaconda] [notebooks]", ],
                  ]
            
            res = setup_jenkins_server(js,
                                       anaconda=r"C:\\Anaconda3",
                                       anaconda2=r"C:\\Anaconda2",
                                       winpython=None,
                                       modules=modules,
                                       fLOG=fLOG,
                                       overwrite=True,
                                       location=r"c:\\jenkins\\pymy",
                                       prefix="_node_")
        assert len(res) > 0


if __name__ == "__main__":
    unittest.main()