import pandas as pd
import requests


class YKRAreas:
    MUN_CODE = "sourceItem.code"
    MUN_NAME = "sourceItem.classificationItemNames"
    REG_CODE = "targetItem.code"
    REG_NAME = "targetItem.classificationItemNames"

    def __init__(self):
        resp = requests.get(
            "https://data.stat.fi/api/classifications/v2/correspondenceTables/kunta_1_20240101%23maakunta_1_20240101/maps",
            params={"content": "data", "meta": "min", "lang": "fi"},
        )
        columns = [self.MUN_CODE, self.MUN_NAME, self.REG_CODE, self.REG_NAME]

        df = (
            pd.json_normalize(resp.json())[columns]
            if resp.ok
            else pd.DataFrame(columns=columns)
        )
        for col in [self.MUN_NAME, self.REG_NAME]:
            df[col] = df[col].map(self.__get_name_fi)

        self.data = df

    def __get_name_fi(self, names: list[dict]) -> str:
        """From the list of the names in different languages,
        pick the one whose language is Finnish

        :param names: List of the names as dicts. Should contain keys 'lang' and 'name'
        :returns: The name in Finnish, if exists
        """
        return next((name for name in names if name["lang"] == "fi"), {"name": ""})[
            "name"
        ]

    def get_reg_code(self, name: str) -> str:
        """Get the region code corresponding to the name

        :param name: The name of the region
        :returns: The corresponding code of the region
        """
        return list(self.data.loc[self.data[self.REG_NAME] == name][self.REG_CODE])[0]

    def get_mun_code(self, name: str) -> str:
        """Get the municipality code corresponding to the name

        :param name: The name of the municipality
        :returns: The corresponding code of the municipality
        """
        return list(self.data.loc[self.data[self.MUN_NAME] == name][self.MUN_CODE])[0]

    def regions(self) -> list[str]:
        """Get the names of the regions in the data
        :returns: The list of the regions
        """
        return list(self.data[self.REG_NAME].sort_values().unique())

    def municipalities(self, reg: str) -> list[str]:
        """Get the names of the municipalities in the region

        :param reg: The region
        :returns: The list of the municipalities in the region
        """
        return list(
            self.data.loc[self.data[self.REG_CODE] == self.get_reg_code(reg)][
                self.MUN_NAME
            ].sort_values()
        )
