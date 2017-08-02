"""
@file
@brief Customize a Windows Setup for these teachings
"""

import pandas

from pymyinstall.packaged import ensae_fullset, classifiers2string
from pyquickhelper.pandashelper import df2rst


def rst_table_modules(classifier=False):
    """
    produces a table with all modules recommended to do machine learning

    @param      classifier  keep classifiers?
    @return                 string
    """
    mod = ensae_fullset()
    mod.sort()
    df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
    if classifier:
        df = df[["usage", "rst_link", "kind", "version",
                "license", "purpose", "classifier"]]
        df["classifier"] = df.apply(
            lambda row: classifiers2string(row["classifier"]), axis=1)
        df.columns = ["usage", "name", "kind", "version",
                    "license", "purpose", "classifier"]
    else:
        df = df[["usage", "rst_link", "kind", "version",
                "license", "purpose"]]
        df.columns = ["usage", "name", "kind", "version",
                    "license", "purpose"]
    df["lname"] = df["name"].apply(lambda s: s.lower())
    df = df.sort_values("lname").drop("lname", axis=1)
    df = df.reset_index(drop=True).reset_index(drop=False)
    return df2rst(df)
