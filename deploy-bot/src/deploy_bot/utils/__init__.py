from datetime import datetime

import dateutil.parser

default_app_config = "deploy_bot.utils.apps.UtilsConfig"


def parse_isodatetime(val) -> datetime:
    return dateutil.parser.parse(val)
