import pandas as pd
import requests

resp = requests.get(
    "https://data.stat.fi/api/classifications/v2/correspondenceTables/kunta_1_20240101%23maakunta_1_20240101/maps",
    params={"content": "data", "meta": "min", "lang": "fi"},
)

mun_code, mun_name = "sourceItem.code", "sourceItem.classificationItemNames"
reg_code, reg_name = "targetItem.code", "targetItem.classificationItemNames"

df = pd.json_normalize(resp.json())[[mun_code, mun_name, reg_code, reg_name]]


def __get_name_fi(names):
    return next((name for name in names if name["lang"] == "fi"), {"name": ""})["name"]


df[mun_name] = df[mun_name].map(__get_name_fi)
df[reg_name] = df[reg_name].map(__get_name_fi)


def get_reg_code(name):
    return list(df.loc[df[reg_name] == name][reg_code])[0]


def get_mun_code(name):
    return list(df.loc[df[mun_name] == name][mun_code])[0]


def get_reg_names():
    return df[reg_name].sort_values().unique()


def get_mun_names_by_reg(reg):
    return list(df.loc[df[reg_code] == get_reg_code(reg)][mun_name].sort_values())
