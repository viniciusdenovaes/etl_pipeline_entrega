import os

import logger as logger_util
logger = logger_util.getLogger(__name__)


class DataGetter:
    def __init__(self):
        self.url = 'https://github.com/raizen-analytics/data-engineering-test/raw/master/assets/vendas-combustiveis-m3.xls'
        self.file_name = 'vendas-combustiveis-m3.xls'

    def make(self):
        self.get()
        self.convert()

    def get(self):
        os.system(f'wget {self.url}')

    def convert(self):
        logger.info(f'converting {self.file_name}')
        os.system(f'soffice --headless --nologo --norestore --convert-to ods {self.file_name}')


if __name__ == '__main__':
    DataGetter().make()
