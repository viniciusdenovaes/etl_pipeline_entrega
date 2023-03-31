from load import Load


import logger as logger_util
logger = logger_util.getLogger(__name__)


def test():

    load = Load()
    dfs = load.load_all()

    logger.info(f'showing some excel data: {"COMBUSTÍVEL	    ANO	    REGIÃO	        ESTADO	    Jan"}')
    logger.info(f'showing some excel data: {"GASOLINA C (m3)	2000	REGIÃO NORTE	RONDÔNIA	136073,253"}')
    # for df in dfs:
    #     res = df[df['COMBUSTÍVEL'] == 'GASOLINA C (m3)']
    #     print(res)

