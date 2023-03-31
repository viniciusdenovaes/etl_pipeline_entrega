
import logging
import verboselogs

verboselogs.install()


class ColoredFormatter(logging.Formatter):
    reset = "\x1b[39m"

    logs_colors = {
        verboselogs. SPAM:     (grey := "\033[35m"),
        logging.     DEBUG:    (white  := "\033[95m"),
        verboselogs. VERBOSE:  (dark_blue := "\033[34m"),
        logging.     INFO:     (blue := "\033[96m"),
        verboselogs. NOTICE:   (dark_yellow := "\033[33m"),
        logging.     WARNING:  (yellow := "\033[93m"),
        verboselogs. SUCCESS:  (green := "\033[92m"),
        logging.     ERROR:    (red := "\033[91m"),
        logging.     CRITICAL: (dark_red := "\033[31m"),
    }

    def __init__(self, fmt: str = '%(asctime)s %(levelname)-8s [%(name)-70s] "%(message)s"', datefmt: str = '%Y-%m-%d %H:%M:%S'):
        super().__init__(fmt=fmt, datefmt=datefmt)

    def format(self, record: logging.LogRecord) -> str:
        s = super(ColoredFormatter, self).format(record)
        color_code = ColoredFormatter.logs_colors.get(record.levelno)
        s = color_code + s + ColoredFormatter.reset
        return s


# noinspection PyTypeChecker
# noinspection PyPep8Naming
def getLogger(name: str) -> verboselogs.VerboseLogger:
    return logging.getLogger(name)


def init_root_logger(level=logging.INFO):
    logger = logging.getLogger('')
    logger.setLevel(level)


    ch = logging.StreamHandler()
    ch.setLevel(level)

    formatter = ColoredFormatter(fmt='%(asctime)s %(levelname)-8s [%(name)-40s] "%(message)s"', datefmt='%Y-%m-%d %H:%M:%S')

    ch.setFormatter(formatter)
    logger.addHandler(ch)



def teste():
    logger: verboselogs.VerboseLogger = getLogger(__name__)
    init_root_logger(verboselogs.SPAM)
    logger.spam('spam log')
    logger.debug('debug log')
    logger.verbose('verbose log')
    logger.info('info log')
    logger.notice('notice log')
    logger.warning('warning log')
    logger.success('success log')
    logger.error('error log')
    logger.critical('critical log')


if __name__ == '__main__':
    teste()

