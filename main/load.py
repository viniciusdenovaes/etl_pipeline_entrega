import os
from pathlib import Path
from typing import List, Tuple

import pandas as pd

import logger as logger_util
logger = logger_util.getLogger(__name__)

path = Path(__file__).parent


class Load:
    def __init__(self):
        self.diesel_sheet_name = 'DPCache_m3_2'
        self.oilder_sheet_name = 'DPCache_m3'

        self.sheet_file = Path('vendas-combustiveis-m3.ods')

    def load(self, sheet_path: Path, book: str) -> pd.DataFrame:
        logger.info(f'loading diesel from sheet {sheet_path} and book {book}')
        return pd.read_excel(sheet_path, book)


    def load_all(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        return self.load_diesel(), self.load_oilder()


    def load_diesel(self) -> pd.DataFrame:
        sheet = path/self.sheet_file
        book = self.diesel_sheet_name
        df = self.load(sheet, book)
        df.name = 'diesel book'
        return df


    def load_oilder(self):
        sheet = path/self.sheet_file
        book = self.oilder_sheet_name
        df = self.load(sheet, book)
        df.name = 'oil derivative book'
        return df


