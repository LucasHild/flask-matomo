import logging

logger = logging.getLogger("flask_matomo")


class MatomoError(Exception):
    pass


from .core import Matomo
