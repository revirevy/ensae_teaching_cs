#-*- coding: utf-8 -*-
"""
@brief      test log(time=51s)
"""

import sys
import os
import unittest
import re
import shutil

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

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a


class TestNotebookRunner1a_correction (unittest.TestCase):

    def test_notebook_runner_correction_1_7(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook1a_correction_1_7")
        keepnote = ls_notebooks("td1a")
        assert len(keepnote) > 0

        cp = os.path.join(temp, "..", "data", "seance4_excel.txt")
        shutil.copy(cp, temp)
        cp = os.path.join(temp, "..", "data", "seance4_excel.xlsx")
        shutil.copy(cp, temp)

        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "_12" not in n
                                and "session6." not in n
                                and "session8." not in n
                                and "session9." not in n
                                and "session_10." not in n
                                and "session_11." not in n
                                and "correction" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        assert len(res) > 0
        fails = [(os.path.split(k)[-1], v)
                 for k, v in sorted(res.items()) if not v[0]]
        for f in fails:
            fLOG(f)
        if len(fails) > 0:
            raise fails[0][1][1]

if __name__ == "__main__":
    unittest.main()
