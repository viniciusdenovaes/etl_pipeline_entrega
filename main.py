import pandas as pd

from load import Load
from transform import Transform
from save import save
from download import DataGetter

import logging
import logger as logger_util

logger = logger_util.getLogger(__name__)
logger_util.init_root_logger(logging.INFO)

if __name__ == '__main__':

    logger.info(f'importing data')
    DataGetter().make()
    logger.success(f'data imported')

    logger.info(f'In main, calling load')
    load = Load()
    dfs = load.load_all()

    logger.info(f'In main, all dataframes in pandas loaded')
    logger.info(f'In main, calling transform')
    t = Transform()

    for df in dfs:
        df: pd.DataFrame
        logger.info(f'In main, loop to add df {df.name} to transform')
        t.add_raw_df(df)

    logger.info('getting final tables of transform')
    df = t.get_final_table()
    logger.success('final table successfully made')

    logger.info('saving table')
    save(df)
    logger.success('table successfully saved')

